# Realm Royale Triggerbot

This project is a simple **triggerbot** designed for **Realm Royale**. It detects red colors on the screen within a specified region, simulating a click when the right mouse button is pressed.

## Features

- Detects enemies by identifying red hues within a defined region.
- Simulates a mouse click upon detection and right-click press.
- Small, frameless UI built with **Flet**.

## Requirements

- Python 3.8 or higher
- Libraries:
  ```
  opencv-python
  numpy
  mss
  pyautogui
  pynput
  flet
  pywin32
  ```

## Installation

Install the required dependencies:

```bash
pip install opencv-python numpy mss pyautogui pynput flet pywin32
```

## How to Use

1. Clone this repository or copy the script into your project folder.
2. Ensure all dependencies are installed.
3. Run the script:

   ```bash
   python triggerbot.py
   ```

4. The bot will activate, detecting targets and performing clicks when the right mouse button is pressed.

## Code Explanation

The bot captures the center of the screen and detects red hues using HSV color thresholds. If the target is detected and the right mouse button is pressed, it performs a mouse click.

## Video Demonstration

Watch the demonstration video on YouTube:

[![Watch the video](https://pics.freeicons.io/uploads/icons/png/16741343401556273568-512.png)](https://youtu.be/yahBp6p12mk?si=F_fXHILQEVcFlNXR)


## Disclaimer

**This project is for educational purposes only. Use it responsibly and ensure it complies with the terms and conditions of the game.**

## License

This project is licensed under the MIT License. Feel free to use and modify the code as needed.

## Credits

Developed by **LostSouls**.

[Telegram](https://t.me/lostsouls_crypto)
