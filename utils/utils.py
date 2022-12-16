from functools import wraps

def catch(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return str(e), 500
    return decorated_function
