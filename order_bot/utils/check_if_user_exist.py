from asgiref.sync import sync_to_async
from users.models import Client


async def handle_user_existence(telegram_id):
    try:
        user = await sync_to_async(Client.objects.get)(telegram_id=telegram_id)
        return True
    except Client.DoesNotExist:
        return False
