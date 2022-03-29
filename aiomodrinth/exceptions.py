class ObjectNotFound(Exception):
    def __init__(self, object_type: str):
        super().__init__(f"{object_type} not found")


class InvalidToken(Exception):
    def __init__(self):
        super().__init__("Token is not correct or you don't have permissions")


class InvalidUser(Exception):
    def __init__(self):
        super().__init__("Not enough rights to perform the action or invalid username/id")
