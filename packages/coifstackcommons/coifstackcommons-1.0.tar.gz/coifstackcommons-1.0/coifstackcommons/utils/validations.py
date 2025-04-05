import re

def validate_password( password: str ) -> bool: 
    """
    Validates a password based on the following criteria:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    """
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):  # At least one uppercase letter
        return False
    if not re.search(r"[a-z]", password):  # At least one lowercase letter
        return False
    return True


def validate_fullname(fullname: str) -> bool:
    """
    Validates a full name based on the following criteria:
    - Only contains letters and spaces
    - Has at least two words (first and last name)
    - Each word starts with an uppercase letter
    """
    if not re.fullmatch(r"[A-Z][a-z]+(?: [A-Z][a-z]+)+", fullname):
        return False
    return True


def validate_company_name( company_name: str) -> bool:
    """
    Validates a company name based on the following criteria:
    - Only contains letters, numbers, spaces, and common symbols like &,-,.
    - Must start with a letter
    - Minimum 2 characters long
    - Cannot contain special characters except &, -, and .
    """
    
    if len(company_name) < 2:  # Must be at least 2 characters long
        return False
    
    if not re.match(r"^[A-Za-z]", company_name):  # Must start with a letter
        return False
    
    if not re.fullmatch(r"[A-Za-z0-9&\-. ]+", company_name):  # Allowed characters
        return False
    
    return True
