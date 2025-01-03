  <h1 style="color: purple;">Realm Royale Triggerbot</h1>
  <p>
      This project is a simple <strong>triggerbot</strong> designed for <strong>Realm Royale</strong>. It detects red colors on the screen within a specified region, simulating a click when the right mouse button is pressed.
  </p>

  <h2>Features</h2>
  <ul>
      <li>Detects enemies by identifying red hues within a defined region.</li>
      <li>Simulates a mouse click upon detection and right-click press.</li>
      <li>Small, frameless UI built with <strong>Flet</strong>.</li>
  </ul>

  <h2>Requirements</h2>
  <ul>
      <li>Python 3.8 or higher</li>
      <li>Libraries: <code>opencv-python</code>, <code>numpy</code>, <code>mss</code>, <code>pyautogui</code>, <code>pynput</code>, <code>flet</code>, <code>pywin32</code></li>
  </ul>

  <h2>Installation</h2>
  <pre>
      <code>
      pip install opencv-python numpy mss pyautogui pynput flet pywin32
      </code>
  </pre>

  <h2>How to Use</h2>
  <ol>
      <li>Clone this repository or copy the script into your project folder.</li>
      <li>Ensure all dependencies are installed.</li>
      <li>Run the script:</li>
      <pre><code>python triggerbot.py</code></pre>
      <li>The bot will activate, detecting targets and performing clicks when the right mouse button is pressed.</li>
  </ol>

  <h2>Code Explanation</h2>
  <p>
      The bot captures the center of the screen and detects red hues using HSV color thresholds.
      If the target is detected and the right mouse button is pressed, it performs a mouse click.
  </p>

  <h2>Disclaimer</h2>
  <p style="color: red;">
      This project is for educational purposes only. Use it responsibly and ensure it complies with the terms and conditions of the game.
  </p>

  <h2>License</h2>
  <p>This project is licensed under the MIT License. Feel free to use and modify the code as needed.</p>

  <h2>Credits</h2>
  <p>Developed by <strong>LostSouls</strong>.</p>
  https://t.me/lostsouls_crypto
