def error_response(message: str):
    return {
        'message': message,
    }, 500