# Challenge ครั้งที่ 3: กดปุ่มเปลี่ยนโหมด 3 โหมด (เฉลยสำหรับครู)
#   โหมด 0: ดับ/เงียบ
#   โหมด 1: LED กระพริบ
#   โหมด 2: LED ติดค้าง + buzzer ดังสั้น ๆ ทุก 2 วินาที

from machine import Pin
import time

button = Pin(4, Pin.IN, Pin.PULL_UP)
led = Pin(5, Pin.OUT)
buzzer = Pin(18, Pin.OUT)

mode = 0
last_press = 0
blink_state = False
last_blink = 0
last_beep = 0

while True:
    now = time.ticks_ms()

    # ตรวจปุ่ม + debounce: รับการกดใหม่เมื่อห่างจากครั้งก่อนเกิน 300ms
    if button.value() == 0 and time.ticks_diff(now, last_press) > 300:
        mode = (mode + 1) % 3
        print("Mode:", mode)
        last_press = now
        led.off()
        buzzer.off()

    if mode == 0:
        led.off()
        buzzer.off()

    elif mode == 1:
        if time.ticks_diff(now, last_blink) > 500:
            blink_state = not blink_state
            led.value(blink_state)
            last_blink = now

    elif mode == 2:
        led.on()
        if time.ticks_diff(now, last_beep) > 2000:
            buzzer.on()
            time.sleep(0.1)
            buzzer.off()
            last_beep = now

    time.sleep(0.02)
