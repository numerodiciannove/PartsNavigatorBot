from typing import List

from asgiref.sync import sync_to_async

from orders.models import Order
from users.models import Client, Car


@sync_to_async
def get_user_by_telegram_id(telegram_id):
    try:
        user = Client.objects.get(telegram_id=telegram_id)
        return user
    except Client.DoesNotExist:
        return None


@sync_to_async
def add_new_vin_code(telegram_id, vin_code):
    try:
        user = Client.objects.get(telegram_id=telegram_id)
        car = Car.objects.create(
            owner=user,
            vin_code=vin_code
        )
        car.save()
        return car
    except Client.DoesNotExist:
        return None


@sync_to_async
def get_user_cars(telegram_id: int):
    try:
        user = Client.objects.get(telegram_id=telegram_id)
        cars = Car.objects.filter(owner=user)
        return list(cars)
    except Client.DoesNotExist:
        return None


@sync_to_async
def delete_car_by_vin_code(vin_code):
    try:
        car = Car.objects.get(vin_code=vin_code)
        car.delete()
        return True
    except Car.DoesNotExist:
        return False


@sync_to_async
def get_user_cars_sync(telegram_user_id):
    try:
        cars = Car.objects.filter(owner__telegram_id=telegram_user_id).all()
        return list(cars)
    except Car.DoesNotExist:
        return []


@sync_to_async
def fetch_user_cars(telegram_user_id: int) -> List[Car]:
    return list(Car.objects.filter(owner__telegram_id=telegram_user_id))


@sync_to_async
def create_order_db(vin_code, sales_department, description=None):
    try:
        car = Car.objects.get(vin_code=vin_code)
        order = Order.objects.create(
            car=car,
            description=description
        )
        order.sales_department.add(sales_department)
        order.save()
        return order
    except Car.DoesNotExist:
        return None


@sync_to_async
def user_update_name(user_telegram_id, user_first_name):
    user = Client.objects.get(telegram_id=user_telegram_id)
    user.first_name = user_first_name
    user.save()


@sync_to_async
def user_update_phone(user_telegram_id, user_phone):
    user = Client.objects.get(telegram_id=user_telegram_id)
    user.phone_number = user_phone
    user.save()
