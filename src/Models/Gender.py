from src.Models.Base import *


class Genders(Base):
    id = PrimaryKeyField()
    gender = CharField(max_length=50)
