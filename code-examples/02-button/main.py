# 02-button: กดปุ่มแล้วไฟติด — ระบบ input → decision → output แรก
# วงจร:
#   Button: GPIO 4 → ปุ่ม → GND (ใช้ pull-up ภายใน: ปล่อย = 1, กด = 0)
#   LED:    GPIO 5 → ตัวต้านทาน 220Ω → LED → GND

from machine import Pin
import time

button = Pin(4, Pin.IN, Pin.PULL_UP)
led = Pin(5, Pin.OUT)

while True:
    if button.value() == 0:   # ปุ่มถูกกด
        led.on()
    else:
        led.off()
    time.sleep(0.05)
