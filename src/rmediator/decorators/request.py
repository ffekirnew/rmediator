def request(cls):
    if "response" not in cls.__dict__:
        raise AttributeError(
            f"Request class cannot be registered; {cls} must contain attribute 'response' to signify the response expected for this request."
        )

    cls.rmediator_decorated_request = True

    return cls
