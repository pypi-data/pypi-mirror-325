import threading
import time
import random
import argparse
from pynput.mouse import Controller, Button
from pynput.keyboard import Controller as KeyboardController, Key, KeyCode, Listener
import pyautogui
import math

# Disabling failsafe
pyautogui.FAILSAFE = False

# Initialize mouse and keyboard controllers
mouse = Controller()
keyboard_controller = KeyboardController()

# Flags for automation behavior
automation_running = False
enable_clicks = False
switch_tabs = False
enable_scrolling = False
enable_mouse_movement = False
enable_tab_pressing = False

# Modifier key state tracking
modifiers = {"ctrl": False, "shift": False}


def executable():
    global automation_running, enable_clicks, switch_tabs, enable_scrolling, enable_mouse_movement, enable_tab_pressing

    # Parse arguments
    parser = argparse.ArgumentParser(description="Mouse Jiggler with automation features")
    parser.add_argument("--enable-clicks", action="store_true", help="Allow mouse clicks during automation")
    parser.add_argument("--enable-tab-switching", action="store_true", help="Enable automatic Ctrl+Tab tab switching")
    parser.add_argument("--enable-scrolling", action="store_true", help="Enable automatic scrolling")
    parser.add_argument("--enable-mouse-movement", action="store_true", help="Enable automatic mouse movement")
    parser.add_argument("--enable-tab-pressing", action="store_true", help="Enable pressing Tab key")
    args = parser.parse_args()

    enable_clicks = args.enable_clicks
    switch_tabs = args.enable_tab_switching
    enable_scrolling = args.enable_scrolling
    enable_mouse_movement = args.enable_mouse_movement
    enable_tab_pressing = args.enable_tab_pressing

    def enable_automation():
        global automation_running
        automation_running = True
        print("Automation enabled.")

    def disable_automation():
        global automation_running
        automation_running = False
        print("Automation disabled.")

    def emergency_shutdown():
        print("Emergency shutdown activated. Exiting script.")
        exit(0)

    def weighted_random_step(max_distance):
        return random.choice([-max_distance, max_distance])

    def smooth_mouse_move(start, end, duration):
        x_start, y_start = start
        x_end, y_end = end

        distance = math.sqrt((x_end - x_start) ** 2 + (y_end - y_start) ** 2)
        steps = max(int(distance / 2), 500)  # Increase steps for longer distances

        control_x1 = x_start + (x_end - x_start) / 3 + random.uniform(-100, 100)
        control_y1 = y_start + (y_end - y_start) / 3 + random.uniform(-100, 100)

        control_x2 = x_start + 2 * (x_end - x_start) / 3 + random.uniform(-100, 100)
        control_y2 = y_start + (y_end - y_start) / 3 + random.uniform(-100, 100)

        control_point1 = (control_x1, control_y1)
        control_point2 = (control_x2, control_y2)

        def cubic_bezier_curve(p0, p1, p2, p3, t):
            return (
                (1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0],
                (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1]
            )

        for i in range(steps + 1):
            if not automation_running:
                return
            
            t = i / steps
            ease_t = 0.5 * (1 - math.cos(math.pi * t))  # Smoother easing function

            x, y = cubic_bezier_curve(start, control_point1, control_point2, end, ease_t)
            mouse.position = (x, y)
            time.sleep((duration / steps) * (0.8 + random.uniform(0, 0.2)))  # Slight variation for realism

    def mouse_automation():
        if not enable_mouse_movement:
            return
        screen_width, screen_height = pyautogui.size()
        min_x, max_x = 0, screen_width - 10
        min_y, max_y = 0, int(screen_height * 0.95)

        while True:
            if not automation_running:
                time.sleep(0.1)
                continue

            current_pos = mouse.position
            max_distance = random.randint(int(screen_width * 0.2), int(screen_width * 0.4))

            next_pos = (
                min(max(min_x, current_pos[0] + weighted_random_step(max_distance)), max_x),
                min(max(min_y, current_pos[1] + weighted_random_step(max_distance)), max_y)
            )

            smooth_mouse_move(current_pos, next_pos, random.uniform(2.0, 8.0))
            time.sleep(random.uniform(3, 6))

            if enable_clicks and random.random() < 0.5:
                if not automation_running:
                    return
                button = Button.left if random.random() < 0.7 else Button.right
                mouse.click(button)
                print(f"{'Left' if button == Button.left else 'Right'} click at {mouse.position}")

    def keyboard_automation():
        while True:
            if not automation_running:
                time.sleep(0.1)
                continue

            if enable_tab_pressing:
                keyboard_controller.press(Key.tab)
                keyboard_controller.release(Key.tab)
                print("Pressed Tab")
                time.sleep(random.uniform(2, 5))

            if switch_tabs:
                keyboard_controller.press(Key.ctrl)
                keyboard_controller.press(Key.tab)
                keyboard_controller.release(Key.tab)
                keyboard_controller.release(Key.ctrl)
                print("Pressed Ctrl + Tab")
                time.sleep(random.uniform(5, 10))

    def smooth_scroll(amount, duration):
        steps = max(abs(amount) * 3, 30)  
        step_duration = duration / steps
        direction = 1 if amount > 0 else -1  

        for i in range(steps):
            if not automation_running:
                return
            
            factor = 0.5 * (1 - math.cos(math.pi * (i / steps)))  
            step_amount = max(1, round(factor * abs(amount) / steps)) * direction
            
            pyautogui.scroll(step_amount)
            time.sleep(step_duration)

    def scroll_automation():
        if not enable_scrolling:
            return
        while True:
            if not automation_running:
                time.sleep(0.1)
                continue
            
            # Introduce a small delay to avoid conflicts
            time.sleep(0.5)  

            scroll_amount = random.choice([-1, 1]) * random.randint(5, 15)
            smooth_scroll(scroll_amount, random.uniform(1, 2))
            print(f"Scrolled {'up' if scroll_amount > 0 else 'down'} by {abs(scroll_amount)}")

            # Another delay after scrolling
            time.sleep(random.uniform(2, 4))

    def on_press(key):
        global modifiers
        if key == Key.ctrl:
            modifiers["ctrl"] = True
        elif key == Key.shift:
            modifiers["shift"] = True
        if key == KeyCode.from_char('u') and modifiers["ctrl"] and modifiers["shift"]:
            enable_automation()
        elif key == KeyCode.from_char('k') and modifiers["ctrl"] and modifiers["shift"]:
            disable_automation()
        elif key == Key.f1:
            emergency_shutdown()

    def on_release(key):
        global modifiers
        if key == Key.ctrl:
            modifiers["ctrl"] = False
        elif key == Key.shift:
            modifiers["shift"] = False

    listener = Listener(on_press=on_press, on_release=on_release)
    listener.start()

    threading.Thread(target=mouse_automation, daemon=True).start()
    threading.Thread(target=keyboard_automation, daemon=True).start()
    threading.Thread(target=scroll_automation, daemon=True).start()

    print("Press Control + Shift + U to enable automation.")
    print("Press Control + Shift + K to disable automation.")
    print("Press F1 for an emergency shutdown.")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting script.")


if __name__ == "__main__":
    executable()
