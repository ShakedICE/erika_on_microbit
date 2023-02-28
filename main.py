def on_button_pressed_a():
    global song
    if song_mode == 1 and song > 0:
        song += -1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global song_mode, song
    if song_mode == 0:
        basic.show_icon(IconNames.EIGTH_NOTE)
        basic.pause(1000)
        basic.clear_screen()
        song_mode = 1
        if song_mode == 1:
            song = 1
    else:
        if song == 1:
            music.play_tone(277, music.beat(BeatFraction.WHOLE))
            music.play_tone(294, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(440, music.beat(BeatFraction.WHOLE))
            music.play_tone(440, music.beat(BeatFraction.WHOLE))
            music.play_tone(554, music.beat(BeatFraction.WHOLE))
            music.play_tone(554, music.beat(BeatFraction.WHOLE))
            basic.pause(100)
            music.play_tone(494, music.beat(BeatFraction.WHOLE))
            music.play_tone(440, music.beat(BeatFraction.WHOLE))
            basic.pause(100)
            music.play_tone(415, music.beat(BeatFraction.WHOLE))
            music.play_tone(440, music.beat(BeatFraction.WHOLE))
            music.play_tone(494, music.beat(BeatFraction.WHOLE))
            basic.pause(100)
            music.play_tone(554, music.beat(BeatFraction.WHOLE))
            music.play_tone(494, music.beat(BeatFraction.WHOLE))
            music.play_tone(440, music.beat(BeatFraction.WHOLE))
            basic.pause(100)
            music.play_tone(277, music.beat(BeatFraction.WHOLE))
            music.play_tone(294, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(330, music.beat(BeatFraction.WHOLE))
            music.play_tone(440, music.beat(BeatFraction.WHOLE))
            music.play_tone(440, music.beat(BeatFraction.WHOLE))
            music.play_tone(554, music.beat(BeatFraction.WHOLE))
            music.play_tone(554, music.beat(BeatFraction.WHOLE))
            music.play_tone(494, music.beat(BeatFraction.WHOLE))
            music.play_tone(440, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global song
    if song_mode == 1:
        song += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

song_mode = 0
song = 0
song = 0
song_mode = 0

def on_forever():
    if song == 2:
        images.create_image("""
            . # # . .
                        . . . # .
                        . . # . .
                        . # . . .
                        . # # # .
        """).show_image(0)
basic.forever(on_forever)

def on_forever2():
    if song == 1:
        images.create_image("""
            . . . . .
                        . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
        """).show_image(0)
basic.forever(on_forever2)

def on_forever3():
    if song == 3:
        images.create_image("""
            . # # . .
                        . . . # .
                        . . # . .
                        . . . # .
                        . # # . .
        """).show_image(0)
basic.forever(on_forever3)
