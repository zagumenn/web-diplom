from src.Models.Order import Orders

class OrderController:

    @classmethod
    def get(cls):
        return Orders.select()

    @classmethod
    def add(cls, user_id, driver_id, car_id, data, price, starting_place, end_place):
        Orders.create(user_id = user_id, driver_id = driver_id, car_id = car_id, data = data,
                      price = price, starting_place = starting_place, end_place = end_place, status_id = 2)

    @classmethod
    def update(cls, id_status, id_order):
        Orders.update({Orders.status_id: id_status}).where(Orders.id == id_order).execute()

    @classmethod
    def delete(cls, id):
        Orders.delete_by_id(id)


if __name__ == "__main__":
    print("---------")
    print(OrderController.delete(1))