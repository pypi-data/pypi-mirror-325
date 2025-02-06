from __future__ import annotations

from pynput import keyboard


class KeyboardMonitor:
    def __init__(self) -> None:
        self.is_paused = False
        self.is_quit = False
        self.listener = None

    def start(self) -> None:
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop(self) -> None:
        if self.listener:
            self.listener.stop()
        self.is_quit = True

    def on_press(self, key: keyboard.Key | keyboard.KeyCode | None) -> None:
        try:
            if key == keyboard.KeyCode.from_char("p"):
                self.is_paused = not self.is_paused
            if key == keyboard.KeyCode.from_char("q"):
                self.stop()
        except AttributeError:
            pass
