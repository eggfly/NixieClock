import PiShiftPy as shift
import time
shift.init(chain_number=2)
i = 0

LED_RED    = 0b1010000000000000
LED_GREEN  = 0b1100000000000000
LED_BLUE   = 0b0110000000000000
DIGIT_1    = 0b0001000000000000
DIGIT_2    = 0b0000100000000000
DIGIT_2    = 0b0000100000000000
CLOCK_UP   = 0b0000000000000100
CLOCK_DOWN = 0b0000000000000010

def run():
    shift.write(LED_RED | LED_GREEN | LED_BLUE | DIGIT_2)
    shift.write(LED_RED ^ DIGIT_2)
    shift.write(LED_GREEN ^ DIGIT_1)
    shift.write(LED_BLUE ^ CLOCK_DOWN)
    shift.write_latch()
while True:
    run()
    time.sleep(1)
    i += 1
