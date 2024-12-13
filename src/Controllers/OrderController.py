from src.Models.Order import *

class OrderController:
    @classmethod
    def get(cls):
        return Orders.select()

    @ classmethod
    def delete(cls, id):
        Orders.delete_by_id(id)


if __name__ == "__main__":
    print("Контролер заказов")

