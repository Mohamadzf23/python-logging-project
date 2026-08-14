from logger_config import logger


class InvalidUsernameError(Exception):
    pass


def create_user(username):
    username = username.strip()

    if username == "":
        raise InvalidUsernameError("Username cannot be empty")

    logger.info("User created successfully")