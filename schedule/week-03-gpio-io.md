# ครั้งที่ 3: GPIO + Input/Output

> **เป้าหมาย:** เข้าใจและสร้างระบบ input → decision → output พื้นฐาน

## โครงเวลา (120 นาที)

| ช่วง | เวลา | กิจกรรม |
|---|---|---|
| 1 | 25 นาที | อธิบาย GPIO, pull-up/pull-down, breadboard + demo ปุ่มกดไฟติด |
| 2 | 65 นาที | ต่อ LED ภายนอก → ต่อ button → ต่อ buzzer → เขียน if-else |
| 3 | 20 นาที | **Team Challenge: 3 โหมด** + log |
| 4 | 10 นาที | สรุป + exit ticket |

## Concept หลัก

```text
INPUT (button) → DECISION (if-else) → OUTPUT (LED/buzzer)
```

นี่คือโครงเดียวกับระบบอัจฉริยะทุกระบบ — สัปดาห์หน้าแค่เปลี่ยน button เป็น sensor

## วงจรที่ต้องต่อ

⚠️ **ถอด USB ก่อนต่อวงจรทุกครั้ง และ peer-check ก่อนเสียบ**

1. **LED ภายนอก**: GPIO 5 → ตัวต้านทาน 220Ω → LED → GND
2. **Button**: GPIO 4 → button → GND (ใช้ pull-up ภายใน)
3. **Buzzer**: GPIO 18 → buzzer → GND

## โค้ดหลัก

ดูตัวอย่างเต็มที่ [`code-examples/02-button/`](../code-examples/02-button/) และ [`code-examples/03-buzzer/`](../code-examples/03-buzzer/)

```python
from machine import Pin
import time

button = Pin(4, Pin.IN, Pin.PULL_UP)   # กด = 0, ปล่อย = 1
led = Pin(5, Pin.OUT)

while True:
    if button.value() == 0:    # ปุ่มถูกกด
        led.on()
    else:
        led.off()
    time.sleep(0.05)
```

## Mini Challenge ระหว่างเรียน

- กดปุ่มแล้วไฟติด ✅
- กดปุ่มแล้วเสียงดัง ✅
- กดปุ่มแล้วไฟติด **และ** เสียงดังพร้อมกัน ✅

## 🏆 Team Challenge: "กดปุ่มเปลี่ยนโหมด"

กดปุ่ม 1 ครั้ง = เปลี่ยนโหมด วนไป 3 โหมด:

| โหมด | พฤติกรรม |
|---|---|
| 0 | ทุกอย่างดับ/เงียบ |
| 1 | LED กระพริบ |
| 2 | LED ติดค้าง + buzzer ดังเตือนสั้น ๆ ทุก 2 วินาที |

ใบ้: ใช้ตัวแปร `mode` นับ 0→1→2→0 และระวัง "กด 1 ครั้งแต่เครื่องอ่านได้หลายครั้ง" (debounce — ใส่ `time.sleep(0.2)` หลังตรวจพบการกด)

ทีมแรกที่ทำครบ 3 โหมดและอธิบาย debounce ได้ = ผู้ชนะ

## ชิ้นงานที่ต้องส่ง

- [ ] ระบบ input → decision → output ทำงานได้ (ครูเช็ค)
- [ ] Challenge 3 โหมดผ่าน
- [ ] ถ่ายรูปวงจร + โค้ดลง `submissions/team-XX/`
- [ ] log 5 บรรทัด

## Exit Ticket

"ถ้าเปลี่ยน button เป็น sensor วัดแสง ระบบของเราจะกลายเป็นระบบอะไรได้บ้าง"

## ✨ Bonus Challenge

เพิ่มโหมดที่ 4: กดปุ่ม **ค้างเกิน 2 วินาที** → เข้าสู่โหมด "ฉุกเฉิน" ไฟกระพริบเร็ว + เสียงดังต่อเนื่อง
