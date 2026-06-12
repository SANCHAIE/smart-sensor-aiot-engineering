# ครั้งที่ 8: Final Project Build Sprint

> **เป้าหมาย:** รวมทุกอย่างที่เรียนมาเป็น prototype ของทีมเอง

## โครงเวลา (120 นาที)

| ช่วง | เวลา | กิจกรรม |
|---|---|---|
| 1 | 15 นาที | ทบทวน Problem Canvas จากครั้งที่ 1 + เกณฑ์ final project |
| 2 | 80 นาที | **Build Sprint**: system diagram → ต่อวงจร → รวมโค้ด → README |
| 3 | 15 นาที | **Team Challenge: 90-Second Demo** |
| 4 | 10 นาที | วางแผนงานค้างสำหรับครั้งหน้า + log |

## เกณฑ์ขั้นต่ำของ Final Project

ระบบของทุกทีมต้องมีครบ:

```text
[SENSOR อย่างน้อย 1 ตัว] → [LOGIC ที่มี threshold จากข้อมูลจริง] → [OUTPUT แจ้งเตือน]
```

ส่วนเสริมที่เพิ่มคะแนน: dashboard, 3 ระดับการแจ้งเตือน, sensor 2 ตัว, data logging ต่อเนื่อง

## ตัวอย่างโจทย์ (เลือกของทีมเองได้)

| ระบบ | Sensor | Logic | Output |
|---|---|---|---|
| Smart Classroom | DHT | ร้อนเกิน 32°C | เตือนเปิดแอร์/พัดลม |
| Smart Light | LDR | มืดแล้วแต่ไฟยังเปิด/ปิด | เตือน + dashboard |
| Smart Parking | Ultrasonic | มีรถจอด < 20 ซม. | ไฟแสดงช่องว่าง |
| Water Tank Monitor | Ultrasonic | น้ำเหลือน้อย | buzzer + web |
| Plant Monitor | DHT + LDR | ร้อน/แสงไม่พอ | แจ้งเตือนรดน้ำ/ย้ายที่ |

## ขั้นตอน Build Sprint

1. **ตัดสินใจสุดท้าย** (10 นาที): โจทย์อะไร ใช้ sensor อะไร — เขียนลง README ทันที ห้ามเปลี่ยนอีก
2. **วาด System Diagram** (15 นาที): ใช้ [template](../worksheets/system-diagram-template.md)
3. **แบ่งงานตามบทบาท** แล้วทำขนาน:
   - Hardware Lead: ต่อวงจรจริง
   - Code Lead: รวมโค้ด sensor + logic + output (+ web)
   - Data & Docs Lead: เริ่ม README ทีม + เตรียมแผนเก็บข้อมูล
4. **รวมระบบ** แล้วลองรันจริงอย่างน้อย 1 รอบ
5. ใช้ [final-project-template](../code-examples/09-final-project-template/) เป็นโครงโค้ดเริ่มต้นได้

## 🏆 Team Challenge: "90-Second Demo"

ปิดคาบด้วยการ demo ระบบของทีมให้เพื่อนดูภายใน **90 วินาที**:
- ระบบต้องตอบสนองต่อเหตุการณ์จริงอย่างน้อย 1 ครั้ง (ไม่ใช่แค่เปิดโค้ดให้ดู)
- บอกให้ได้ว่า "ยังขาดอะไร" อีก 1 อย่าง

ทุกทีมที่ demo ได้ = ผ่าน ทีมที่ระบบนิ่งสุดได้ดาวพิเศษ

## ชิ้นงานที่ต้องส่ง

- [ ] **Prototype v1** ทำงานได้อย่างน้อย 1 วงจรเต็ม sense → think → act
- [ ] **System Diagram** (ถ่ายรูป/ไฟล์ลง `teams/team-XX/`)
- [ ] **README draft** ตามหัวข้อใน [team README template](../teams/README.md)
- [ ] log 5 บรรทัด + รายการงานค้างสำหรับครั้งที่ 9

## Exit Ticket

"ความเสี่ยงที่ใหญ่ที่สุดที่อาจทำให้ demo day ของทีมพังคืออะไร และจะป้องกันยังไง"
