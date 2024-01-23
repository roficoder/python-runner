import pyautogui
import time
import random


def scroll_half_screen_randomly():
    # Scroll randomly up or down approximately half of the screen height
    screen_width, screen_height = pyautogui.size()
    scroll_amount = int(screen_height / 2)
   
    # Randomly determine the direction of the scroll
    if random.random() < 0.5:
        pyautogui.scroll(scroll_amount)
    else:
        pyautogui.scroll(-scroll_amount)


def move_cursor_slightly():
    # Move the cursor slightly within the screen boundaries
    screen_width, screen_height = pyautogui.size()
    current_x, current_y = pyautogui.position()
    move_x = random.randint(-50, 50)  # Adjust the range for x-axis movement
    move_y = random.randint(-50, 50)  # Adjust the range for y-axis movement
    new_x = max(0, min(screen_width - 1, current_x + move_x))
    new_y = max(0, min(screen_height - 1, current_y + move_y))
    pyautogui.moveTo(new_x, new_y, duration=0.5)


if __name__ == "__main__":
    # Wait for a minute before starting the random movements
    time.sleep(10)


    # Continuously perform random movements
    while True:
        scroll_half_screen_randomly()
        move_cursor_slightly()
        # Adjust the sleep time based on how frequently you want the actions to occur
        time.sleep(5)  # Change this value to set the interval between movements



