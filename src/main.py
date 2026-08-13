from logger_config import logger
from users import create_user, InvalidUsernameError


try:
    create_user("Mohamadreza")
    create_user("   ")
except InvalidUsernameError:
    logger.exception("Invalid username")