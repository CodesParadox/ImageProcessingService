# Image Processing Telegram Bot

This project is an image processing service that uses a Telegram bot to interact with users. Users can send images to the bot and choose a filter to apply to the image. The bot then processes the image and sends it back to the user.

## Project Structure

The project is structured as follows:

- `polybot/bot.py`: Contains the `Bot`, `QuoteBot`, and `ImageProcessingBot` classes. The `Bot` class is a simple echo bot, the `QuoteBot` class extends the `Bot` class to quote incoming messages, and the `ImageProcessingBot` class extends the `Bot` class to process incoming photo messages.
- `polybot/img_proc.py`: Contains the `Img` class, which is used for image processing. The `Img` class has methods for various image filters, such as blur, contour, rotate, segment, salt and pepper, and concat.
- `polybot/app.py`: The main entry point of the application. It's a Flask web server that uses an instance of the `Bot` class to handle incoming messages.
- `polybot/test`: Contains unit tests for each filter and the Telegram bot.

## Image Filters

The `Img` class in `polybot/img_proc.py` provides the following image filters:

- `blur()`: Blurs the image.
- `contour()`: Applies a contour effect to the image.
- `rotate()`: Rotates the image clockwise.
- `segment()`: Partitions the image into regions where the pixels have similar attributes.
- `salt_n_pepper()`: Adds "salt and pepper" noise to the image.
- `concat()`: Concatenates two images together horizontally.

## Telegram Bot

The `ImageProcessingBot` class in `polybot/bot.py` handles incoming photo messages from users. It processes the photos according to the caption field provided with the message and sends the processed image back to the user.


## Prerequisites

Before running the bot, make sure you have the following installed:

- Python 3.6 or later
- Ngrok (for exposing the local server to the internet)


This project is an image processing Telegram bot built with Python and the pyTelegramBotAPI library. The bot allows users to send photos, and it can perform various image processing operations on those photos, such as blurring, contouring, rotating, segmenting, adding salt and pepper noise, and concatenating images.

## Prerequisites

Before running the bot, make sure you have the following installed:

- Python 3.6 or later
- Ngrok (for exposing the local server to the internet)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/CodesParadox/ImageProcessingService.git
```

2. Navigate to the project directory:

```bash
cd ImageProcessingService
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

1. Obtain a Telegram Bot token by creating a new bot using the BotFather on Telegram.

2. Install and authenticate Ngrok by following the instructions [here](https://ngrok.com/docs/getting-started/#step-2-install-the-ngrok-agent).

3. Set the following environment variables:

   - `TELEGRAM_TOKEN`: Your Telegram Bot token.
   - `TELEGRAM_APP_URL`: The public URL provided by Ngrok (leave it blank for now).

   On Linux or macOS, you can set the environment variables like this:

   ```bash
   export TELEGRAM_TOKEN="your_telegram_bot_token"
   export TELEGRAM_APP_URL=""
   ```

   On Windows, use the following commands:

   ```
   set TELEGRAM_TOKEN="your_telegram_bot_token"
   set TELEGRAM_APP_URL=""
   ```

## Running the Bot

1. Start Ngrok with the following command:

```bash
ngrok http 8443
```

2. Copy the public URL provided by Ngrok (e.g., `https://abcd.ngrok.io`).

3. Update the `TELEGRAM_APP_URL` environment variable with the copied URL.

4. Run the bot:

```bash
python app.py
```

5. In the Telegram app, search for your bot and start sending photos to it. The bot will process the photos based on the provided captions and send back the processed images.


## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

This README provides an overview of the project, instructions for installation and configuration, steps to run the bot, a list of available filters, and information about contributing and licensing.

You can customize this README further by adding any additional details specific to your implementation, such as information about the `Img` class and its methods, examples of usage, or any other relevant information you'd like to include.
## Running the Bot

To run the bot, you need to set the `TELEGRAM_TOKEN` and `TELEGRAM_APP_URL` environment variables to your Telegram bot token and the public URL of your app, respectively. Then, you can run `polybot/app.py` to start the bot.

## Testing

You can run the unit tests in the `polybot/test` directory to test the image filters and the Telegram bot.

## Contributing

Contributions are welcome. Please feel free to submit a pull request or open an issue.# Image processing service
