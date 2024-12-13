from src.Models.Base import *
from src.Models.Role import Roles
from flask_login import UserMixin


class Users(UserMixin,Base):
    id = PrimaryKeyField()
    fullname = CharField(max_length=50)
    login = CharField(unique=True, max_length=50)
    password = CharField(max_length = 300)
    role_id = ForeignKeyField(Roles)