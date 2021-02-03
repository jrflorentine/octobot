input.set_sound_threshold(SoundThreshold.LOUD, 130)

def on_forever():
    while input.button_is_pressed(Button.A):
        servos.P1.run(20)
    servos.P1.stop()
    while input.button_is_pressed(Button.B):
        servos.P1.run(-20)
    servos.P1.stop()
    if input.logo_is_pressed():
        servos.P1.run(20)
        basic.pause(2000)
        servos.P1.stop()
basic.forever(on_forever)
