def success_response(data: any, message: str):
    return {
        'message': message,
        'data': data
    }, 200