import os
import uuid
import time
import asyncio
import aiohttp
import datetime
import logging
from typing import Any, Dict, Optional, List

from pydantic import BaseModel

from dhisana.utils.execute_command_mock import execute_task_command_mock
from dhisana.utils.generate_structured_output_internal import get_structured_output_internal

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_task_agent_access_token(tool_config: Optional[List[Dict]] = None) -> str:
    """
    Retrieves the TaskAgent access token from the provided tool configuration or environment.
    Raises:
        ValueError: If the token is not found.
    """
    logger.debug("Attempting to get TASK_AGENT_API_KEY from tool_config or environment.")

    task_agent_api_key: Optional[str] = None
    if tool_config:
        task_agent_config = next(
            (item for item in tool_config if item.get("name") == "dhisana_workflow_tools"), None
        )
        if task_agent_config:
            config_map = {
                c["name"]: c["value"]
                for c in task_agent_config.get("configuration", [])
                if c
            }
            task_agent_api_key = config_map.get("apiKey")

    # Fallback to environment variable
    task_agent_api_key = task_agent_api_key or os.getenv("TASK_AGENT_API_KEY", "test")
    if not task_agent_api_key:
        raise ValueError("TASK_AGENT_API_KEY not found in config or env.")
    
    logger.debug("TASK_AGENT_API_KEY successfully retrieved.")
    return task_agent_api_key


async def execute_task_command(
    command_name: str,
    command_args: Dict[str, Any],
    max_timeout: float = 2400,
    tool_config: Optional[List[Dict]] = None
) -> Dict[str, Any]:
    """
    1. Enqueues a task to the TaskAgent service using /add_agent_task.
    2. Polls /get_agent_task_result until completion or until max_timeout has passed.
    3. Removes task from status queue and pending queue.
    4. Returns the command result.

    This function is asynchronous and will yield control during sleep intervals,
    allowing other tasks to run concurrently.
    """
    logger.debug("Preparing to execute task command: %s", command_name)
    logger.debug("Command args: %s", command_args)

    # ----------------------------------------------------------------
    # CONFIG & PREP
    # ----------------------------------------------------------------
    task_agent_api_key = get_task_agent_access_token(tool_config)
    request_id = str(uuid.uuid4())
    api_base_url = os.environ.get("AGENT_SERVICE_URL", "https://api-agent.dhisana.ai/v1")

    payload = {
        "command_request_id": request_id,
        "command_name": command_name,
        "command_args": command_args
    }

    add_task_url = f"{api_base_url}/add_agent_task"
    get_task_result_url = f"{api_base_url}/get_agent_task_result"
    remove_task_result_url = f"{api_base_url}/remove_agent_task_result"

    headers = {
        "Authorization": f"Bearer {task_agent_api_key}",
        "Content-Type": "application/json"
    }

    final_result: Dict[str, Any] = {}

    async with aiohttp.ClientSession() as session:
        # ----------------------------------------------------------------
        # 1) ENQUEUE THE TASK
        # ----------------------------------------------------------------
        logger.debug("Enqueueing task with request_id %s at %s", request_id, add_task_url)
        async with session.post(add_task_url, json=payload, headers=headers) as response:
            if response.status != 200:
                raise Exception(f"Failed to add task. Status code: {response.status}")
            add_resp = await response.json()
            logger.debug("Response from adding task: %s", add_resp)
            if add_resp.get("status") != "OK":
                raise Exception(f"Error adding task: {add_resp}")

        # ----------------------------------------------------------------
        # 2) POLL UNTIL THE TASK IS COMPLETED OR TIMEOUT
        # ----------------------------------------------------------------
        start_time = time.time()
        end_time = start_time + max_timeout

        logger.debug("Polling for task completion (timeout %s seconds)...", max_timeout)
        while time.time() < end_time:
            async with session.post(
                get_task_result_url,
                params={"request_id": request_id},
                headers=headers
            ) as poll_response:
                if poll_response.status != 200:
                    raise Exception(
                        f"Failed to poll task result. Status code: {poll_response.status}"
                    )
                poll_data = await poll_response.json()

            logger.debug("Polling data: %s", poll_data)

            if poll_data.get("status") == "ERROR":
                msg = poll_data.get("message", "Unknown error during polling")
                raise Exception(f"Task {request_id} returned an error: {msg}")

            current_status = poll_data.get("current_status", "")
            if current_status == "completed":
                final_result = poll_data.get("result", {})
                logger.debug("Task %s completed successfully. Result: %s", request_id, final_result)
                break

            await asyncio.sleep(20)
        else:
            # If we exit the while-loop normally (no break), it's a timeout
            raise TimeoutError(
                f"Task {request_id} did not complete within {max_timeout} seconds."
            )

        # ----------------------------------------------------------------
        # 3) REMOVE THE TASK RESULTS FROM THE STATUS QUEUE
        # ----------------------------------------------------------------
        logger.debug("Removing task result from queue: %s", request_id)
        async with session.delete(
            remove_task_result_url,
            params={"request_id": request_id},
            headers=headers
        ) as remove_res_status:
            if remove_res_status.status != 200:
                raise Exception(
                    f"Failed to remove task result. Status code: {remove_res_status.status}"
                )
            remove_status_resp = await remove_res_status.json()
            logger.debug("Response from removing task result: %s", remove_status_resp)
            if remove_status_resp.get("status") != "OK":
                raise Exception(f"Error removing task result: {remove_status_resp}")

    # ----------------------------------------------------------------
    # 4) RETURN THE RESULT
    # ----------------------------------------------------------------
    logger.debug("Returning final result for command: %s", command_name)
    return final_result


class ShouldExecuteCommand(BaseModel):
    should_execute: bool
    reason_for_skipping_execution: str


async def execute_task(
    command_name: str,
    command_args: Optional[Dict[str, Any]] = None,
    max_timeout: float = 2400,
    lead_info: Dict[str, Any] = None,
    campaign_context: Dict[str, Any] = None,
    tool_config: Optional[List[Dict]] = None
) -> Dict[str, Any]:
    """
    High-level function that checks if a command should be executed, then
    executes it if the constraint is met. Otherwise, returns a skip message.
    """
    command_args = command_args or {}
    lead_info = lead_info or {}
    campaign_context = campaign_context or {}
    if lead_info.get("user_linkedin_url"): 
        command_args["user_linkedin_url"] = lead_info.get("user_linkedin_url")
    if lead_info.get("user_linkedin_salesnav_url"):
        command_args["user_linkedin_salesnav_url"] = lead_info.get("user_linkedin_salesnav_url")
        
    if not command_args.get("user_linkedin_url") and not command_args.get("user_linkedin_salesnav_url"):
        raise ValueError("Both LinkedIn and Sales Navigator URLs are empty.")
    
    logger.debug("Condition met. Executing command: %s", command_name)
    # result = await execute_task_command_mock(
    #     command_name,
    #     command_args,
    #     max_timeout,
    #     tool_config
    # )
    result = await execute_task_command(
        command_name,
        command_args,
        max_timeout,
        tool_config
    )
    logger.debug("Command execution result: %s", result)
    return result



