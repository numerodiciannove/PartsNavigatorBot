# PartsNavigatorBot

PartsNavigatorBot is a Telegram bot built with Python, Django, and Aiogram. It allows users to manage their cars and create repair orders directly through Telegram.

## Features

- User registration and authentication
- Add, delete, and view user cars
- Create repair orders and parts requests
- Notifications and alerts via Telegram

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/PartsNavigatorBot.git
    cd PartsNavigatorBot
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables in a `.env` file with the necessary configurations:
    ```env
    TELEGRAM_BOT_TOKEN=your_telegram_bot_token
    DATABASE_URL=your_database_url
    ```

5. Apply the Django migrations:
    ```bash
    python manage.py migrate
    ```

6. Create a superuser for Django admin:
    ```bash
    python manage.py createsuperuser
    ```

7. Run the development server:
    ```bash
    python manage.py runserver
    ```

8. Start the bot:
    ```bash
    python manage.py order_bot
    ```

## Usage

- Interact with the bot via Telegram to add, delete, and view your cars.
- Create repair orders directly through the bot.
- Receive notifications and updates on your orders.

## Project Structure

- `manage.py`: Django's command-line utility for administrative tasks.
- `order_bot/`: Contains the main bot logic and handlers.
  - `handlers/`: Defines the bot's command and callback query handlers.
  - `keyboards/`: Contains the inline keyboard builders for bot interactions.
  - `utils/`: Utility functions for database operations and other helpers.
- `users/`: Django app managing user data.
- `cars/`: Django app managing car data.
- `orders/`: Django app managing repair orders.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
