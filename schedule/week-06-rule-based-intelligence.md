# ครั้งที่ 6: Rule-based Intelligence

> **เป้าหมาย:** สร้างระบบตัดสินใจอัตโนมัติ โดยใช้ threshold ที่ได้จาก **ข้อมูลจริง** ของครั้งที่แล้ว

## โครงเวลา (120 นาที)

| ช่วง | เวลา | กิจกรรม |
|---|---|---|
| 1 | 20 นาที | Rule-based intelligence คืออะไร + ทำไม threshold จากข้อมูลดีกว่าเดา |
| 2 | 70 นาที | สร้างเงื่อนไขแจ้งเตือน → ต่อ LED/buzzer → ปรับ threshold จากข้อมูลจริง |
| 3 | 20 นาที | **Team Challenge: 3 ระดับการแจ้งเตือน** + log |
| 4 | 10 นาที | สรุป: rule-based vs machine learning ต่างกันอย่างไร + exit ticket |

## Concept หลัก

"ความฉลาด" ระดับแรกของเครื่องคือ **กฎ (rule)**:

```python
if temperature > 30:
    alert = "HOT"
else:
    alert = "NORMAL"
```

จุดที่ทำให้มันเป็น "วิศวกรรม" คือ **เลข 30 มาจากไหน** — ทีมที่ใช้ข้อมูลจริงจากครั้งที่ 5 จะตอบได้ ทีมที่เดาจะตอบไม่ได้

## กิจกรรม

1. เปิด insight + threshold ที่ทีมหาไว้เมื่อครั้งที่แล้ว
2. เขียนระบบแจ้งเตือนเต็มวงจร:

```python
from machine import ADC, Pin
import time

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)
led = Pin(5, Pin.OUT)
buzzer = Pin(18, Pin.OUT)

THRESHOLD = 3000    # ← ค่านี้ต้องมาจาก data.csv ของทีม!

while True:
    value = ldr.read()
    if value > THRESHOLD:
        print(value, "ALERT: too dark!")
        led.on()
        buzzer.on()
    else:
        print(value, "NORMAL")
        led.off()
        buzzer.off()
    time.sleep(1)
```

3. ทดสอบกับสถานการณ์จริง → ถ้าแจ้งเตือนพลาด/แจ้งมั่ว ให้ปรับ threshold แล้วจดว่าปรับเพราะอะไร

## 🏆 Team Challenge: "ระบบแจ้งเตือน 3 ระดับ"

อัปเกรดจาก 2 สถานะ เป็น 3 ระดับ:

| ระดับ | เงื่อนไข | Output |
|---|---|---|
| 🟢 NORMAL | ค่าปกติ | เงียบ |
| 🟡 WARNING | เริ่มเข้าใกล้อันตราย | LED กระพริบช้า |
| 🔴 ALERT | เกินขีดอันตราย | LED กระพริบเร็ว + buzzer |

เงื่อนไขพิเศษ: ทั้ง 2 threshold ต้อง **อ้างอิงจากข้อมูลจริง** และทีมต้องอธิบายได้ว่าเลือกอย่างไร
ใบ้: ใช้ `if / elif / else`

## ชิ้นงานที่ต้องส่ง

- [ ] **Smart Alert System v1** ทำงานได้จริง (ครูเช็ค + ทดสอบสด 1 สถานการณ์)
- [ ] โค้ดอัปโหลดลง `teams/team-XX/code/`
- [ ] จดบันทึก: threshold ที่ใช้ + เหตุผล + ปรับกี่ครั้งเพราะอะไร
- [ ] log 5 บรรทัด

## Exit Ticket

"ถ้าระบบเราแจ้งเตือนผิด (false alarm) บ่อย ๆ จะเกิดอะไรขึ้นกับผู้ใช้ และแก้ยังไง"

## ✨ Bonus Challenge

ลด false alarm ด้วย **การเฉลี่ยก่อนตัดสิน**: อ่านค่า 5 ครั้งติดกัน เอาค่าเฉลี่ยมาเทียบ threshold แทนการใช้ค่าเดี่ยว — แล้วทดสอบว่าระบบนิ่งขึ้นจริงไหม
