# Smart Sensor AIoT Engineering

### สร้างระบบอัจฉริยะด้วย ESP32, MicroPython และข้อมูลจาก Sensor

> รายวิชาแบบ Project-based สำหรับนักเรียน ม.5–ม.6 จำนวน 30 คน
> **10 ทีม × ทีมละ 3 คน | 10 ครั้ง × 2 ชั่วโมง (รวม 20 ชั่วโมง)**

---

## 🎯 เป้าหมายของวิชา

เมื่อจบคอร์สนี้ นักเรียนจะสามารถ:

1. เขียนโปรแกรม MicroPython ควบคุม ESP32 ได้
2. ต่อวงจรและอ่านค่าจาก sensor จริง (DHT, LDR, Ultrasonic)
3. เก็บข้อมูล วิเคราะห์ และหา threshold จากข้อมูลจริง
4. สร้างระบบตัดสินใจอัตโนมัติ (Rule-based Intelligence)
5. แสดงผลข้อมูลผ่าน Wi-Fi / Web Dashboard
6. ทดสอบระบบอย่างเป็นระบบ (Testing) แบบวิศวกร
7. นำเสนอผลงานวิศวกรรมต่อสาธารณะ

## 🗺️ แผนการเรียน 10 ครั้ง

| ครั้งที่ | หัวข้อ | ชิ้นงานหลัก | Challenge |
|---|---|---|---|
| 1 | [เปิดโลก AIoT + ตั้งทีม + GitHub](schedule/week-01-aiot-stem-intro.md) | Problem Canvas | ตั้งโจทย์ปัญหาจริงในโรงเรียน |
| 2 | [Setup ESP32 + MicroPython](schedule/week-02-esp32-micropython.md) | Blink LED | ไฟกระพริบ 3 จังหวะ (SOS) |
| 3 | [GPIO + Input/Output](schedule/week-03-gpio-io.md) | ระบบ input → decision → output | กดปุ่มเปลี่ยนโหมด 3 โหมด |
| 4 | [Sensor Reading](schedule/week-04-sensor-reading.md) | ตารางข้อมูล 20+ แถว | ทำนายค่าก่อนวัดจริง |
| 5 | [Data Logging + Visualization](schedule/week-05-data-visualization.md) | data.csv + กราฟ + insight | หา "ค่าผิดปกติ" ในข้อมูลทีมอื่น |
| 6 | [Rule-based Intelligence](schedule/week-06-rule-based-intelligence.md) | Smart Alert System v1 | ระบบ 3 ระดับ NORMAL/WARN/ALERT |
| 7 | [Wi-Fi / Web Dashboard](schedule/week-07-wifi-dashboard.md) | Web แสดงค่า sensor | หน้า web เปลี่ยนสีตามสถานะ |
| 8 | [Final Project Build Sprint](schedule/week-08-project-build.md) | Prototype v1 + System Diagram | Demo ภายใน 90 วินาที |
| 9 | [Testing + Improvement + Pitch](schedule/week-09-testing-pitch.md) | Testing Table + Prototype v2 | หา bug ของทีมอื่นให้เจอ |
| 10 | [Demo Day](schedule/week-10-demo-day.md) | Final Demo + Presentation | — |

## ⏱️ โครงเวลาในแต่ละครั้ง (120 นาที)

| ช่วง | เวลา | กิจกรรม |
|---|---|---|
| 1 | 20–30 นาที | อธิบาย concept + demo สั้น |
| 2 | 60–70 นาที | ลงมือทำตามใบงาน / coding / ต่อวงจร |
| 3 | 20–25 นาที | Team Challenge + บันทึกผลลง GitHub |
| 4 | 5–10 นาที | สรุป + exit ticket |

## 📁 โครงสร้าง Repository

```text
smart-sensor-aiot-engineering/
├── README.md              ← คุณอยู่ที่นี่
├── syllabus.md            ← รายละเอียดวิชา + เกณฑ์การให้คะแนน
├── schedule/              ← แผนการสอนรายครั้ง (10 ครั้ง)
├── code-examples/         ← โค้ดตัวอย่าง MicroPython ทุกหัวข้อ
├── worksheets/            ← ใบงาน / template ต่าง ๆ
├── project-template/      ← โครงโค้ด + ใบงาน สำหรับ final project (copy ไปใช้ได้เลย)
└── submissions/           ← พื้นที่ส่งงานของแต่ละทีม (10 ทีม)
```

## 🧰 อุปกรณ์ต่อทีม

| อุปกรณ์ | จำนวน |
|---|---|
| ESP32 DevKit | 1 |
| Breadboard + สายจัมเปอร์ | 1 ชุด |
| LED + ตัวต้านทาน 220Ω | 3–5 |
| Push button | 2 |
| Buzzer | 1 |
| DHT11/DHT22 (อุณหภูมิ/ความชื้น) | 1 |
| LDR + ตัวต้านทาน 10kΩ (แสง) | 1 |
| HC-SR04 Ultrasonic (ระยะทาง) | 1 |
| สาย USB | 1 |

ซอฟต์แวร์: [Thonny IDE](https://thonny.org/) + [MicroPython firmware สำหรับ ESP32](https://micropython.org/download/esp32/)

## 📤 กติกาการส่งงาน (ระบบ Fork)

1. แต่ละทีมต้อง **Fork repo นี้** ไปยังบัญชี GitHub ของตัวแทนทีม (GitHub Manager ของทีม)
2. แต่ละทีมแก้ไขเฉพาะ folder ของทีมตนเองใน `submissions/team-xx/`
3. **ห้ามแก้ไข** ไฟล์ใน `schedule/`, `worksheets/`, `code-examples/`, `project-template/` ยกเว้นได้รับอนุญาต
4. ทุกครั้งที่ส่งงาน ให้ commit ด้วยข้อความที่สื่อความหมาย
5. การส่งงานทำได้ 2 วิธี
   - ส่ง link fork ผ่าน Google Form
   - เปิด Pull Request กลับมายัง repo กลาง
6. ถ้าเปิด Pull Request ให้ตั้งชื่อว่า `Team xx - Week yy Submission`

ตัวอย่างชื่อ Pull Request

```text
Team 01 - Week 01 Submission
Team 03 - Add STEM Problem Canvas
Team 07 - Week 05 Data Visualization
Team 10 - Final Project Submission
```

ภาพรวม workflow

```text
อาจารย์สร้าง repo กลาง
↓
ทีม fork repo
↓
ทีมแก้เฉพาะ submissions/team-xx/
↓
ทีม commit ทุกสัปดาห์
↓
ส่ง link fork หรือเปิด pull request
↓
อาจารย์ review / merge / ให้ feedback
```

> 💡 ช่วงแรกไม่จำเป็นต้องใช้ command line — แก้ไฟล์/อัปโหลดผ่าน GitHub Web ได้เลย และถ้าติดปัญหาเรื่อง fork/PR ให้ส่งผ่าน Google Form สำรองไว้ก่อน

## 📝 กติกาประจำทุกครั้ง

ทุกทีมต้องเติม log ลง `submissions/team-XX/README.md` (ใน fork ของทีม) ก่อนหมดคาบ อย่างน้อย 5 บรรทัด:

```text
วันนี้ทำอะไร
ต่อวงจรอะไร
โค้ดสำคัญคืออะไร
เจอปัญหาอะไร
ครั้งหน้าจะทำอะไรต่อ
```

## 🚀 เริ่มต้นอย่างไร

1. ตัวแทนทีม (GitHub Manager): **Fork repo นี้** แล้วไปที่โฟลเดอร์ทีมของตัวเองใน [`submissions/`](submissions/)
2. อ่านแผนครั้งที่ 1 ที่ [`schedule/week-01-aiot-stem-intro.md`](schedule/week-01-aiot-stem-intro.md)
3. ดูโค้ดตัวอย่างได้ที่ [`code-examples/`](code-examples/)
4. อ่านกติกาการส่งงานแบบละเอียดที่ [`submissions/README.md`](submissions/README.md)
