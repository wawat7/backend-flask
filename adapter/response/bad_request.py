def bad_request_response(message: str, errors: any):
    return {
        "message": message,
        "errors": errors,
    }, 400
