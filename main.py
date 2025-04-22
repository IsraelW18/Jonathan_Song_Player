from player.melody import get_freqs, get_main_melody, get_break_part, get_second_part
from player.playback import play_notes

def main():
    freqs = get_freqs()
    main_melody = get_main_melody()
    break_part = get_break_part(main_melody)
    second_part = get_second_part(main_melody)

    play_notes(main_melody, freqs)
    play_notes(main_melody[:6], freqs)
    play_notes(break_part, freqs)
    play_notes(second_part, freqs)
    play_notes(main_melody[:6], freqs)
    play_notes(break_part, freqs)

if __name__ == "__main__":
    main()
