from src.Models.Base import *
from src.Models.Car import Cars
from src.Models.Statuses import Statuses
from src.Models.User import Users


class Orders(Base):
    id = PrimaryKeyField()
    driver_id = ForeignKeyField(Users)
    user_id = ForeignKeyField(Users)
    data = DateField()
    price = IntegerField()
    status_id = ForeignKeyField(Statuses)
    car_id = ForeignKeyField(Cars)
    starting_place = CharField()
    end_place = CharField()

