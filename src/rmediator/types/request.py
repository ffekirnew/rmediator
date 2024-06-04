from abc import ABCMeta


class Request(metaclass=ABCMeta):
    response = None
