import winsound
import time
from .utils import clear_console

def play_notes(note_list, freqs, delay=1):
    for i, (note, duration) in enumerate(note_list):
        winsound.Beep(freqs[note], int(duration))
        clear_console()
        bar = "█" * (i + 1)
        print(f"Playing: {note.upper()}  | Duration: {duration} ms")
        print(f"Progress: {bar}")
        time.sleep(delay)
