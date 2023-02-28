input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (song_mode == 1 && song > 0) {
        song += -1
    }
    
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    
    if (song_mode == 0) {
        basic.showIcon(IconNames.EigthNote)
        basic.pause(1000)
        basic.clearScreen()
        song_mode = 1
        if (song_mode == 1) {
            song = 1
        }
        
    } else if (song == 1) {
        music.playTone(277, music.beat(BeatFraction.Whole))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.playTone(554, music.beat(BeatFraction.Whole))
        music.playTone(554, music.beat(BeatFraction.Whole))
        basic.pause(100)
        music.playTone(494, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        basic.pause(100)
        music.playTone(415, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.playTone(494, music.beat(BeatFraction.Whole))
        basic.pause(100)
        music.playTone(554, music.beat(BeatFraction.Whole))
        music.playTone(494, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        basic.pause(100)
        music.playTone(277, music.beat(BeatFraction.Whole))
        music.playTone(294, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(330, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
        music.playTone(554, music.beat(BeatFraction.Whole))
        music.playTone(554, music.beat(BeatFraction.Whole))
        music.playTone(494, music.beat(BeatFraction.Whole))
        music.playTone(440, music.beat(BeatFraction.Whole))
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (song_mode == 1) {
        song += 1
    }
    
})
let song_mode = 0
let song = 0
song = 0
song_mode = 0
basic.forever(function on_forever() {
    if (song == 2) {
        images.createImage(`
            . # # . .
                        . . . # .
                        . . # . .
                        . # . . .
                        . # # # .
        `).showImage(0)
    }
    
})
basic.forever(function on_forever2() {
    if (song == 1) {
        images.createImage(`
            . . . . .
                        . . # . .
                        . # # . .
                        . . # . .
                        . . # . .
        `).showImage(0)
    }
    
})
basic.forever(function on_forever3() {
    if (song == 3) {
        images.createImage(`
            . # # . .
                        . . . # .
                        . . # . .
                        . . . # .
                        . # # . .
        `).showImage(0)
    }
    
})
