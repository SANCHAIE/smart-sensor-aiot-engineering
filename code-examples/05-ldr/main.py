# 05-ldr: อ่านความเข้มแสงด้วย LDR (analog)
# วงจร (voltage divider):
#   3.3V → LDR → จุดกึ่งกลาง → ตัวต้านทาน 10kΩ → GND
#   จุดกึ่งกลาง → GPIO 34 (ขา ADC, input อย่างเดียว)
# แสงมาก → ความต้านทาน LDR ต่ำ → ค่าที่อ่านได้สูง (ขึ้นกับวิธีต่อ อาจกลับด้านได้)

from machine import ADC, Pin
import time

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)    # ขยายช่วงวัดเป็น 0–3.3V → อ่านได้ 0–4095

while True:
    value = ldr.read()
    print("Light level:", value)
    time.sleep(0.5)
