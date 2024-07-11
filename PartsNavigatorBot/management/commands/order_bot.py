import asyncio

from django.core.management.base import BaseCommand
from order_bot.main import main


class Command(BaseCommand):
    """Command to start bot"""

    def handle(self, *args, **options):
        self.stdout.write("Bot started...")

        asyncio.run(main())

        self.stdout.write(self.style.SUCCESS("Bot available!"))
