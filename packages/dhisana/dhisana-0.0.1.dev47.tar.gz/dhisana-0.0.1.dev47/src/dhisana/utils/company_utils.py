import re
import unicodedata

from dhisana.utils.assistant_tool_tag import assistant_tool

import re
import unicodedata

@assistant_tool
def normalize_company_name(company_name: str) -> str:
    """
    Normalize a company name by removing special characters, truncating after specific delimiters,
    removing common legal suffixes, and limiting the length to 64 characters.

    Additionally, if the company name is empty or contains variations of "freelance", 
    "self-employed", or "taking-break", an empty string is returned.

    Parameters:
    - company_name (str): The original company name.

    Returns:
    - str: The normalized company name.
    """
    if not company_name:
        return ""

    normalized_name = company_name.lower()

    # Step 0: Return empty if variations of 'freelance', 'self-employed', or 'taking-break' are detected
    excluded_variations = ["freelanc", "self-employed", "self employed", "taking-break", "taking break"]
    if any(phrase in normalized_name for phrase in excluded_variations):
        return ""

    # Step 1: Remove content after specific delimiters
    normalized_name = re.split(r'[|,]', normalized_name)[0]

    # Step 2: Remove special characters and punctuation
    normalized_name = re.sub(r'[^\w\s]', '', normalized_name)

    # Step 3: Normalize whitespace
    normalized_name = re.sub(r'\s+', ' ', normalized_name).strip()

    # Step 4: Remove common legal suffixes
    suffixes = r'\b(inc|llc|ltd|plc|llp|cic|unlimited|pvt ltd|opc pvt ltd|producer company limited|co|company|corporation|gmbh|plc|pvt|private|limited)\b'
    normalized_name = re.sub(suffixes, '', normalized_name)

    # Step 5: Remove accents
    normalized_name = ''.join(
        c for c in unicodedata.normalize('NFD', normalized_name)
        if unicodedata.category(c) != 'Mn'
    )

    # Step 6: Trim to a maximum length of 64 characters
    normalized_name = normalized_name[:64].strip()

    return normalized_name