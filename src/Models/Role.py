from src.Models.Base import *

class Roles(Base):
    id = PrimaryKeyField()
    name = CharField(unique=True, max_length=20)

