# 04-dht: อ่านอุณหภูมิ + ความชื้นจาก DHT11/DHT22
# วงจร: VCC → 3.3V, GND → GND, DATA → GPIO 15
# (โมดูลบางตัวต้องมีตัวต้านทาน pull-up 10kΩ ระหว่าง DATA กับ VCC — โมดูลสำเร็จมักมีให้แล้ว)

from machine import Pin
import dht
import time

sensor = dht.DHT11(Pin(15))    # ถ้าใช้ DHT22 เปลี่ยนเป็น dht.DHT22(...)

while True:
    try:
        sensor.measure()
        temp = sensor.temperature()    # องศาเซลเซียส
        hum = sensor.humidity()        # เปอร์เซ็นต์
        print("Temp: {} C | Humidity: {} %".format(temp, hum))
    except OSError:
        print("อ่านค่าไม่ได้ ตรวจสายไฟ/ขา DATA")
    time.sleep(2)    # DHT11 อ่านได้ไม่เร็วกว่าทุก 1–2 วินาที
