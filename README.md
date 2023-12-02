# VideoNote2TextBot
## Description:
VideoNote2TextBot is a Telegram bot developed using aiogram 3, asyncpg, and utilizes fast-whisper largev3 int8 for CPU inference. The bot provides functionality for converting video messages into a text format, offering a convenient and efficient way to interact with video content within the messenger.

## Key Features:

### **Transcription of Video Messages**:

The bot accepts video messages from users and uses fast-whisper largev3 int8 to transcribe speech into text.
The transcription result is provided to the user in a convenient text format.
## Technologies Used:

- `aiogram 3`: A library for creating Telegram bots based on asynchronous programming.
- `asyncpg`: A library for working with PostgreSQL using asynchronous queries.
- `fast-whisper largev3 int8`: A model optimized for CPU inference, designed for efficient transcription of audio and video files.
## Advantages:

- **Conversion to Text from Video Messages**: Provides a straightforward method for extracting textual information from videos in Telegram.
- **Efficiency and Speed**: The use of the optimized fast-whisper largev3 int8 model for CPU inference ensures high performance.
## Usage Instructions:

1. Send a video message to the bot on Telegram.
2. The bot will transcribe the video and provide the result in text format.
