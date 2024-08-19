
# playwright-audio-captcha-solver

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.9%2B-green)
![Playwright](https://img.shields.io/badge/Playwright-1.17.0-brightgreen)
![Last Commit](https://img.shields.io/github/last-commit/Kizuno18/playwright-audio-captcha-solver)

## Overview

`playwright-audio-captcha-solver` is a Python-based automation tool designed to streamline the process of solving reCAPTCHAs. This bot leverages the power of Playwright for browser automation and the SpeechRecognition library to transcribe audio CAPTCHAs.

## Features

- **Automated Browser Interaction**: Utilizes Playwright to simulate user actions within a browser, including filling out login forms and interacting with reCAPTCHA.
- **Audio CAPTCHA Downloading**: Automatically downloads audio CAPTCHAs for further processing.
- **Speech Recognition**: Converts the audio CAPTCHA into text using Google's Speech-to-Text API.
- **User-Friendly**: Simple and intuitive command interface with minimal user intervention.

## Requirements

Before running the script, ensure you have the following installed:

- Python 3.9+
- Playwright
- Requests
- SpeechRecognition
- PyAudio (for SpeechRecognition)

You can install the required packages using:

```bash
pip install -r requirements.txt
```

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Kizuno18/playwright-audio-captcha-solver.git
   cd playwright-audio-captcha-solver
   ```

2. **Install Playwright Dependencies**:

   ```bash
   playwright install
   ```

3. **Install Other Python Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Configure Login Information**:

   Update the `email` and `password` variables in the script with your login credentials.

2. **Run the Script**:

   To execute the bot, run:

   ```bash
   python captcha_solver_bot.py
   ```

3. **Interact with reCAPTCHA**:

   The bot will navigate to the login page, fill in the credentials, and wait for your input to solve the CAPTCHA. Press `r` when prompted to solve the CAPTCHA.

4. **Manual Override**:

   If the bot fails to automatically solve the CAPTCHA, you can manually enter the audio CAPTCHA response.

## How It Works

1. **Browser Automation**: The script uses Playwright to automate browser interactions, such as navigating to the login page, filling in credentials, and interacting with reCAPTCHA.
2. **Audio Processing**: Once the audio CAPTCHA is triggered, the script downloads the audio file and processes it using the `SpeechRecognition` library.
3. **Transcription**: The audio file is transcribed into text, which is then entered into the CAPTCHA response field.
4. **Verification**: The bot submits the CAPTCHA response and proceeds with the login.

## Limitations

- **Audio Quality**: The accuracy of the transcription depends on the quality of the audio provided by the CAPTCHA.
- **Anti-bot Measures**: Some websites may have advanced anti-bot measures that could prevent the bot from functioning properly.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For significant changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, feel free to open an issue or contact the repository owner.
