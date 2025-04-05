def base_error(msg: str, code: int = 400) -> dict:
    """
    Generic error response for handling client errors.
    Default HTTP status code: 400 (Bad Request).
    """
    return {"message": msg, "code": code, "status": False}

def base_response(data, msg: str = "Success") -> dict:
    """
    Standard success response format.
    Used for returning successful API responses with data.
    """
    return {"data": data, "message": msg, "status": True}

def unauthorized_response(msg: str = "Unauthorized access") -> dict:
    """
    Response for authentication failures.
    HTTP status code: 401 (Unauthorized).
    """
    return {"message": msg, "code": 401, "status": False}

def forbidden_response(msg: str = "Forbidden: Insufficient permissions") -> dict:
    """
    Response for users with insufficient permissions.
    HTTP status code: 403 (Forbidden).
    """
    return {"message": msg, "code": 403, "status": False}

def not_found_response(msg: str = "Resource not found") -> dict:
    """
    Response for missing resources (e.g., user, product, etc.).
    HTTP status code: 404 (Not Found).
    """
    return {"message": msg, "code": 404, "status": False}

def validation_error_response(errors: dict, msg: str = "Invalid input") -> dict:
    """
    Response for failed validation errors.
    Includes a dictionary of specific validation error messages.
    HTTP status code: 422 (Unprocessable Entity).
    """
    return {"message": msg, "code": 422, "status": False, "errors": errors}

def server_error_response(msg: str = "Internal Server Error") -> dict:
    """
    Response for unexpected internal server errors.
    HTTP status code: 500 (Internal Server Error).
    """
    return {"message": msg, "code": 500, "status": False}

def conflict_response(msg: str = "Conflict: Resource already exists") -> dict:
    """
    Response when a request conflicts with an existing resource.
    Example: Trying to register an already existing email.
    HTTP status code: 409 (Conflict).
    """
    return {"message": msg, "code": 409, "status": False}

def created_response(data, msg: str = "Resource created successfully") -> dict:
    """
    Response for successful resource creation.
    HTTP status code: 201 (Created).
    """
    return {"data": data, "message": msg, "code": 201, "status": True}

def no_content_response(msg: str = "No content available") -> dict:
    """
    Response for successful requests where no content needs to be returned.
    HTTP status code: 204 (No Content).
    """
    return {"message": msg, "code": 204, "status": True}
