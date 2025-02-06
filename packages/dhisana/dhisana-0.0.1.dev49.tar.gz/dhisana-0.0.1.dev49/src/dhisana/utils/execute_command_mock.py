# Mock execute_task_command for local testing
import asyncio
import logging
from typing import Any, Dict, List, Optional
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# ------------------------------------------------------------------
# 1) Mock command handlers
# ------------------------------------------------------------------

async def view_linkedin_profile(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mocks viewing a LinkedIn profile, returning a success status.
    """
    logger.debug("Mock: view_linkedin_profile called with args=%s", args)
    user_url = args.get("user_linkedin_salesnav_url")
    # You could check 'args["lead"]["viewed_last"]' or other fields in real code
    return {
        "status": "SUCCESS",
        "action_taken": "viewed_profile",
        "profile_url": user_url
    }

async def send_connection_request(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mocks sending a LinkedIn connection request.
    """
    logger.debug("Mock: send_connection_request called with args=%s", args)
    lead_name = args.get("lead", {}).get("full_name")
    return {
        "status": "SUCCESS",
        "action_taken": "connection_request_sent",
        "lead": lead_name
    }

async def send_linkedin_message(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mocks sending a LinkedIn message.
    """
    logger.debug("Mock: send_linkedin_message called with args=%s", args)
    lead_name = args.get("lead", {}).get("full_name")
    conversation_snippet = args.get("lead", {}).get("linked_in_responses", [])
    campaign_context = args.get("campaign_context", {})
    # You might do logic here, e.g. "if user asked for more info, respond with pitch..."
    return {
        "status": "SUCCESS",
        "action_taken": "message_sent",
        "lead": lead_name,
        "previous_conversation": conversation_snippet,
        "context_used": campaign_context
    }

async def like_recent_post(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mocks liking a recent LinkedIn post from a lead.
    """
    logger.debug("Mock: like_recent_post called with args=%s", args)
    lead_name = args.get("lead", {}).get("full_name")
    return {
        "status": "SUCCESS",
        "action_taken": "liked_post",
        "lead": lead_name
    }

async def send_email(args: Dict[str, Any]) -> Dict[str, Any]:
    """
    Mocks sending an email to a lead.
    In a real case, you might integrate with your email service API.
    """
    logger.debug("Mock: send_email called with args=%s", args)
    lead_email = args.get("lead", {}).get("email")
    subject = f"Quick follow-up re: {args.get('campaign_context', {}).get('product_name', 'Your product')}"
    return {
        "status": "SUCCESS",
        "action_taken": "email_sent",
        "recipient": lead_email,
        "subject": subject
    }

# ------------------------------------------------------------------
# 2) The mock version of execute_task_command that picks the command
# ------------------------------------------------------------------

async def execute_task_command_mock(
    command_name: str,
    command_args: Dict[str, Any],
    max_timeout: float = 2400,
    condition_trigger: Optional[str] = None,
    tool_config: Optional[List[Dict[str, Any]]] = None
) -> Dict[str, Any]:
    """
    A mock version of execute_task_command that directly calls
    the local mock functions instead of communicating with an API.
    """
    logger.debug("Mock execute_task_command called. Command=%s, Args=%s", command_name, command_args)
    # Simulate a short wait time
    await asyncio.sleep(0.1)

    # Switch-like logic for commands
    if command_name == "view_linkedin_profile":
        return await view_linkedin_profile(command_args)
    elif command_name == "send_connection_request":
        return await send_connection_request(command_args)
    elif command_name == "send_linkedin_message":
        return await send_linkedin_message(command_args)
    elif command_name == "like_recent_post":
        return await like_recent_post(command_args)
    elif command_name == "send_email":
        return await send_email(command_args)
    else:
        logger.debug("Unrecognized command: %s. Returning status=UNKNOWN", command_name)
        return {
            "status": "UNKNOWN_COMMAND",
            "message": f"No mock handler for command '{command_name}'"
        }
