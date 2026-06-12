# ครั้งที่ 2: Setup ESP32 + MicroPython

> **เป้าหมาย:** ทุกทีมรันโค้ดแรกบน ESP32 ได้จริง

## โครงเวลา (120 นาที)

| ช่วง | เวลา | กิจกรรม |
|---|---|---|
| 1 | 25 นาที | รู้จัก ESP32 + MicroPython + demo flash firmware |
| 2 | 65 นาที | ติดตั้ง Thonny → flash firmware → run `print()` → Blink LED |
| 3 | 20 นาที | **Team Challenge: SOS Blink** + บันทึก log |
| 4 | 10 นาที | สรุป + exit ticket |

## Concept หลัก

- ESP32 คือคอมพิวเตอร์จิ๋วที่มีขา GPIO + Wi-Fi ในตัว
- MicroPython คือ Python ที่รันบนชิปได้โดยตรง
- `main.py` คือไฟล์ที่ ESP32 รันอัตโนมัติเมื่อเปิดเครื่อง
- REPL คือที่ทดลองคำสั่งสด ๆ ทีละบรรทัด

## ขั้นตอน (ตามใบงาน)

1. ติดตั้ง/เปิด [Thonny](https://thonny.org/)
2. เสียบ ESP32 → Thonny: `Tools → Options → Interpreter → MicroPython (ESP32)`
3. Flash firmware (Thonny ทำให้ได้จากเมนู `Install or update MicroPython`)
4. ทดสอบใน REPL:
   ```python
   print("Hello, Team 01!")
   ```
5. ทำ Blink LED — ดูโค้ดที่ [`code-examples/01-blink/`](../code-examples/01-blink/)

```python
from machine import Pin
import time

led = Pin(2, Pin.OUT)   # LED บนบอร์ด ESP32 ส่วนใหญ่อยู่ขา 2

while True:
    led.on()
    time.sleep(0.5)
    led.off()
    time.sleep(0.5)
```

## 🏆 Team Challenge: "SOS Blink"

ทำไฟกระพริบ **3 จังหวะแบบรหัสมอร์ส SOS**: สั้น-สั้น-สั้น / ยาว-ยาว-ยาว / สั้น-สั้น-สั้น แล้วเว้น 2 วินาที วนซ้ำ

เกณฑ์:
- สั้น = ติด 0.2 วินาที, ยาว = ติด 0.8 วินาที
- **ห้าม copy-paste `led.on()` เกิน 3 ครั้ง** → บังคับให้ใช้ function + loop

ใบ้: เขียน `def blink(duration):` แล้วเรียกใช้ซ้ำ

## ชิ้นงานที่ต้องส่ง

- [ ] ไฟ LED กระพริบได้ (ครูเช็คหน้างาน)
- [ ] SOS Blink ผ่าน (ถ่ายวิดีโอสั้น/ครูเซ็นรับรอง)
- [ ] บันทึกขั้นตอน setup ของทีมลง `teams/team-XX/` (เขียนแบบที่ทีมอื่นอ่านแล้วทำตามได้)
- [ ] log 5 บรรทัด

## Exit Ticket

"ถ้าเสียบ ESP32 แล้ว Thonny มองไม่เห็นบอร์ด จะลองแก้อะไรเป็นอย่างแรก"

## ✨ Bonus Challenge

ทำให้ความเร็วกระพริบ **ค่อย ๆ เร็วขึ้น** ทุกรอบ (ใบ้: ใช้ตัวแปร delay ที่ลดลงเรื่อย ๆ)

## ปัญหาที่เจอบ่อย (ครูเตรียมรับมือ)

| อาการ | สาเหตุ/ทางแก้ |
|---|---|
| Thonny ไม่เห็นบอร์ด | ขาด driver CP210x/CH340 → ติดตั้ง driver, ลองเปลี่ยนสาย USB (บางเส้นชาร์จอย่างเดียว) |
| Flash ไม่ผ่าน | กดปุ่ม BOOT ค้างตอนเริ่ม flash |
| โค้ดเก่ารันวนไม่หยุด | กด Ctrl+C ใน REPL หรือกดปุ่ม Stop ใน Thonny |
