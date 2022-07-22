import time
from pynput import keyboard
from random import randint

FRAME_INTERVAL_SEC = 1
MAX_PIXELS = 1000
UP_KEY = "u"
BOUNCE = 10
DECREASE = 2


class KeyboardMonitor:
    def on_press(self, key):
        try:
            self.inputs.append(key.char)
        except AttributeError:
            self.inputs.append(key)

    def on_release(self, key):
        if key == keyboard.Key.esc:
            # Stop listener
            print("Stoping listener")
            return False

    def __init__(self, inputs):
        self.inputs = inputs
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()


class Position:
    def __init__(self, pos=None):
        if pos:
            self.y = pos
        else:
            self.y = randint(0, MAX_PIXELS)

    def update(self, current_inputs):
        did_flap = UP_KEY in current_inputs
        if did_flap:
            self.y = min(MAX_PIXELS, self.y + BOUNCE)
        else:
            self.y = max(0, self.y - DECREASE)

    def __repr__(self):
        return f"Altitude = {self.y}"


def main():
    position = Position()
    current_inputs = []
    KeyboardMonitor(current_inputs)
    while True:
        position.update(current_inputs)
        print(position)
        current_inputs.clear()
        time.sleep(FRAME_INTERVAL_SEC)


if __name__ == "__main__":
    main()
