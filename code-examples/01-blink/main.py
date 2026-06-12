# 01-blink: ไฟ LED กระพริบ — โปรแกรมแรกบน ESP32
# วงจร: ใช้ LED บนบอร์ด (GPIO 2) ไม่ต้องต่ออะไรเพิ่ม

from machine import Pin
import time

led = Pin(2, Pin.OUT)

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
