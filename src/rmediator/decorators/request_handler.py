def request_handler(cls):
    if "request" not in cls.__dict__:
        raise ValueError(
            f"Request handler class cannot be registered, {cls} must contain attribute 'request' to signify the reequest it handles."
        )

    if "response" not in cls.__dict__:
        raise ValueError(
            f"Request handler class cannot be registered, {cls} must contain attribute 'response' to signify the response it sends after handling request."
        )

    if "handle" not in cls.__dict__:
        raise ValueError(
            f"Request handler class cannot be registered, {cls} must contain method 'handle' that handles the request."
        )

    if cls.request is None:  # type: ignore
        raise ValueError(
            f"Request handler class cannot be registered, {cls} must contain attribute 'request' to signify the request it handles."
        )

    if cls.handle.__annotations__.get("request", None) != cls.request:  # type: ignore
        raise ValueError(
            f"Request handler class cannot be registered, {cls} handle method must have 'request' parameter of type {cls.request}."  # type: ignore
        )

    if cls.handle.__annotations__.get("return", None) != cls.response:  # type: ignore
        raise ValueError(
            f"Request handler class cannot be registered, {cls} handle method must have return type of {cls.response}."  # type: ignore
        )

    cls.rmediator_decorated_request_handler = True

    return cls
