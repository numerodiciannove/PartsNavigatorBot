from asgiref.sync import sync_to_async
from users.models import Client, Car
from order_bot.utils.inline_keyboard_builder import InlineKeyboardBuilder


@sync_to_async
def user_cars_kb(telegram_id):
    try:
        user = Client.objects.get(telegram_id=telegram_id)
        user_cars = Car.objects.filter(owner=user)

        kb = InlineKeyboardBuilder()

        for car in user_cars:
            kb.button(text=f"❌🚙 {car.vin_code}",
                      callback_data=f"delete_car_{car.vin_code}")
            kb.adjust(1)

        return kb.as_markup()
    except Client.DoesNotExist:
        return None
