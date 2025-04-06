from typing import Any, Dict, List, Union

def remove_empty(data: Any) -> Any:
    """
    Recursively remove empty or null-like values from JSON/dict data.
    
    - Removes None or 'null' (case-insensitive) strings.
    - Removes empty strings.
    - Removes empty lists and dicts.
    - Returns `None` if the entire structure becomes empty.
    """
    if isinstance(data, dict):
        cleaned_dict: Dict[str, Any] = {}
        for key, value in data.items():
            cleaned_value = remove_empty(value)
            if cleaned_value is not None:
                cleaned_dict[key] = cleaned_value
        
        # Return None if dictionary is empty after cleaning
        return cleaned_dict if cleaned_dict else None

    elif isinstance(data, list):
        cleaned_list: List[Any] = []
        for item in data:
            cleaned_item = remove_empty(item)
            if cleaned_item is not None:
                cleaned_list.append(cleaned_item)
        
        # Return None if list is empty after cleaning
        return cleaned_list if cleaned_list else None

    else:
        # Base/primitive case
        # Remove None or empty strings or strings "null" (case-insensitive)
        if data is None:
            return None
        if isinstance(data, str):
            if not data.strip() or data.lower() == "null":
                return None
        return data


def cleanup_properties(properties: Dict[str, Any]) -> Dict[str, Any]:
    """
    In-place style: returns a cleaned copy (so the original isn't mutated).
    """
    cleaned = remove_empty(properties)
    return cleaned if cleaned is not None else {}
