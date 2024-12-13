from src.Models.Base import *
from src.Models.Statuses import Statuses
from src.Models.User import Users


class Cars(Base):
    id = PrimaryKeyField()
    brand = CharField()
    model = CharField()
    color = CharField()
    state_number = CharField()