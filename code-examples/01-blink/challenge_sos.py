# Challenge ครั้งที่ 2: SOS Blink (เฉลยสำหรับครู)
# สั้น-สั้น-สั้น / ยาว-ยาว-ยาว / สั้น-สั้น-สั้น เว้น 2 วินาที วนซ้ำ

from machine import Pin
import time

led = Pin(2, Pin.OUT)

SHORT = 0.2
LONG = 0.8
GAP = 0.2


def blink(duration):
    led.on()
    time.sleep(duration)
    led.off()
    time.sleep(GAP)


def blink_pattern(duration, times):
    for _ in range(times):
        blink(duration)


while True:
    blink_pattern(SHORT, 3)   # S
    blink_pattern(LONG, 3)    # O
    blink_pattern(SHORT, 3)   # S
    time.sleep(2)
