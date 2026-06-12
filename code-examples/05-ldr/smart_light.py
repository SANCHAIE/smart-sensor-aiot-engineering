# ตัวอย่างต่อยอด: Smart Light — มืดแล้วไฟติดอัตโนมัติ
# ใช้ค่าเฉลี่ย 5 ครั้งก่อนตัดสินใจ เพื่อลดการกระพริบมั่วจากค่าแกว่ง

from machine import ADC, Pin
import time

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)
led = Pin(5, Pin.OUT)

DARK_THRESHOLD = 1000    # ← ปรับจากข้อมูลจริงของห้องตัวเอง!


def read_average(n=5):
    total = 0
    for _ in range(n):
        total += ldr.read()
        time.sleep(0.05)
    return total / n


while True:
    avg = read_average()
    if avg < DARK_THRESHOLD:
        led.on()
        print(avg, "-> DARK, light ON")
    else:
        led.off()
        print(avg, "-> BRIGHT, light OFF")
    time.sleep(0.5)
