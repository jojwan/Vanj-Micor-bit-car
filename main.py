basic.show_icon(IconNames.HEART)

def on_forever():
    if mbit_小车类.Line_Sensor(mbit_小车类.enPos.LEFT_STATE, mbit_小车类.enLineState.BLACK) and mbit_小车类.Line_Sensor(mbit_小车类.enPos.RIGHT_STATE, mbit_小车类.enLineState.BLACK):
        basic.show_leds("""
            # # . # #
                        # # . # #
                        # # . # #
                        # # . # #
                        # # . # #
        """)
    elif mbit_小车类.Line_Sensor(mbit_小车类.enPos.RIGHT_STATE, mbit_小车类.enLineState.BLACK):
        basic.show_leds("""
            . . . # #
                        . . . # #
                        . . . # #
                        . . . # #
                        . . . # #
        """)
    elif mbit_小车类.Line_Sensor(mbit_小车类.enPos.LEFT_STATE, mbit_小车类.enLineState.BLACK):
        basic.show_leds("""
            # # . . .
                        # # . . .
                        # # . . .
                        # # . . .
                        # # . . .
        """)
    else:
        basic.show_leds("""
            . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
                        . . . . .
        """)
basic.forever(on_forever)
