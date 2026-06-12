# 06-ultrasonic: วัดระยะทางด้วย HC-SR04
# วงจร: VCC → 5V (VIN), GND → GND, Trig → GPIO 26, Echo → GPIO 27
# ⚠️ Echo ของ HC-SR04 ส่ง 5V — ถ้าจะปลอดภัยกับ ESP32 (3.3V) ควรใช้
#    voltage divider (1kΩ + 2kΩ) ที่ขา Echo หรือใช้รุ่น HC-SR04P (3.3V ได้)

from machine import Pin
import time

trig = Pin(26, Pin.OUT)
echo = Pin(27, Pin.IN)


def read_distance_cm():
    # ส่ง pulse สั้น ๆ 10 ไมโครวินาที
    trig.off()
    time.sleep_us(2)
    trig.on()
    time.sleep_us(10)
    trig.off()

    # จับเวลาที่เสียงเดินทางไป-กลับ
    duration = time.ticks_us()
    timeout = duration + 30000          # กันค้างถ้าไม่มีเสียงสะท้อนกลับ
    while echo.value() == 0:
        if time.ticks_us() > timeout:
            return None
    start = time.ticks_us()
    while echo.value() == 1:
        if time.ticks_us() > timeout:
            return None
    end = time.ticks_us()

    # เสียงเร็ว 343 m/s → 0.0343 cm/us หาร 2 เพราะไป-กลับ
    return time.ticks_diff(end, start) * 0.0343 / 2


while True:
    d = read_distance_cm()
    if d is None:
        print("วัดไม่ได้ (ไกลเกิน/ต่อสายผิด)")
    else:
        print("Distance: {:.1f} cm".format(d))
    time.sleep(0.5)
