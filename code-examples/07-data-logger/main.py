# 07-data-logger: เก็บข้อมูล sensor ลงไฟล์ CSV บน ESP32
# ใช้กับครั้งที่ 5 — เปลี่ยน read_sensor() ให้ตรงกับ sensor ของทีม

from machine import ADC, Pin
import time

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

INTERVAL_S = 2     # เก็บทุกกี่วินาที
SAMPLES = 60       # เก็บกี่จุด (60 จุด × 2 วิ = 2 นาที)


def read_sensor():
    return ldr.read()


with open("data.csv", "w") as f:
    f.write("time_s,value\n")
    for i in range(SAMPLES):
        value = read_sensor()
        f.write("{},{}\n".format(i * INTERVAL_S, value))
        print(i * INTERVAL_S, value)
        time.sleep(INTERVAL_S)

print("Done! saved {} samples to data.csv".format(SAMPLES))
print("ดึงไฟล์ผ่าน Thonny: View -> Files -> คลิกขวา data.csv -> Download")
