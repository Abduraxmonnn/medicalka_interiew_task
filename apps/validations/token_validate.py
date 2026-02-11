def auth_token_validate(request) -> dict:
    auth_header = request.headers.get("Authorization")
    if auth_header is None:
        return {"error": "No token provided", 'status_code': 401}

    try:
        prefix, token = auth_header.split(" ")
        if prefix.lower() != "bearer":
            raise ValueError("Invalid token prefix")
    except ValueError:
        return {"error": "Invalid Authorization header", 'status_code': 401}

    return {'prefix': prefix, 'token': token}
