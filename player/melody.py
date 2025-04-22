def get_freqs():
    return {
        "la": 220,
        "si": 247,
        "do": 261,
        "re": 293,
        "mi": 329,
        "fa": 349,
        "sol": 392
    }

def get_main_melody():
    notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"
    return [item.split(",") for item in notes.split("-")]

def get_break_part(main):
    return [
        main[6], main[1], main[0], main[0],
        [main[6][0], '500']
    ]

def get_second_part(main):
    return [
        main[4], main[4], main[4], main[4], main[4],
        main[1], [main[3][0], '500'],
        main[1], main[1], main[1], main[1], main[1],
        main[3], main[-1]
    ]
