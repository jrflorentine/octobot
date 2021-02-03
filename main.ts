basic.forever(function () {
    while (input.buttonIsPressed(Button.A)) {
        servos.P1.run(20)
    }
    servos.P1.stop()
    while (input.buttonIsPressed(Button.B)) {
        servos.P1.run(-20)
    }
    servos.P1.stop()
    if (input.logoIsPressed() && input.soundLevel() > 128) {
        servos.P1.run(20)
        basic.pause(2500)
        servos.P1.stop()
    }
})
