import cv2
import numpy as np
import mss
import pyautogui
from pynput.mouse import Listener
import flet as ft
import win32gui
import win32con

lower_red1 = np.array([0, 100, 100])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([160, 100, 100])
upper_red2 = np.array([180, 255, 255])

WIDTH = 5
HEIGHT = 40

right_button_pressed = False

def on_click(x, y, button, pressed):
    global right_button_pressed
    if button.name == "right":
        right_button_pressed = pressed


def get_tiny_center_region(monitor_width, monitor_height):
    center_x, center_y = monitor_width // 2, monitor_height // 2
    left = center_x - WIDTH // 2
    top = center_y - HEIGHT // 2
    return {"left": left, "top": top, "width": WIDTH, "height": HEIGHT}


def contains_red_color(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv_image, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv_image, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)
    return np.any(red_mask > 0)


def make_window_click_through(hwnd):
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                           ex_style | win32con.WS_EX_LAYERED | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT)
    win32gui.SetLayeredWindowAttributes(hwnd, 0, 0, win32con.LWA_ALPHA)


def main(page: ft.Page):
    global right_button_pressed
    page.window.width = 250
    page.window.height = 75
    page.window.resizable = False
    page.window.frameless = True
    page.window.transparent = True
    page.window.always_on_top = True
    page.window.left = 10
    page.window.top = 10

    hwnd = win32gui.FindWindow(None, page.title)
    make_window_click_through(hwnd)

    title = ft.Text("Realm Royale Triggerbot | LostSouls", color="purple", size=12, weight="bold")
    indicator = ft.Text("Target: Null", color="red", size=12, weight="bold")
    page.add(title)
    page.add(indicator)

    listener = Listener(on_click=on_click)
    listener.start()

    monitor_width, monitor_height = pyautogui.size()
    region = get_tiny_center_region(monitor_width, monitor_height)

    with mss.mss() as sct:
        while True:
            screen_capture = np.array(sct.grab(region))
            target_detected = contains_red_color(screen_capture)

            if target_detected and right_button_pressed:
                pyautogui.click()

            if target_detected:
                indicator.value = "Target: Enemy"
                indicator.color = "green"
            else:
                indicator.value = "Target: Null"
                indicator.color = "red"

            page.update()


if __name__ == "__main__":
    ft.app(target=main)
