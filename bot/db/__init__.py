from .models import Subscribe
from .Users import Users, User
db_file_name = "bot/db/database"
users = Users(db_file_name=db_file_name, table_name="users")
Subscribes = Subscribe()
__all__ = ("User", "Users", "users", "Subscribes")
