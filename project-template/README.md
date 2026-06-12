# Project Template — โครงเริ่มต้นสำหรับ Final Project

ใช้สำหรับ Final Project (ครั้งที่ 8–10) — copy **ทั้งโฟลเดอร์นี้** ไปไว้ใน `submissions/team-XX/` แล้วเติม/แก้ตามทีมของตัวเอง

```text
project-template/
├── README.md          ← ไฟล์นี้
├── problem-canvas.md  ← copy จาก worksheets/stem-problem-canvas.md
├── system-diagram.md  ← copy จาก worksheets/system-diagram-template.md
├── testing-table.md   ← copy จาก worksheets/testing-table.md
├── main.py            ← โครงโค้ด SENSE → THINK → ACT → LOG
└── data.csv           ← ไฟล์ log ผลการทดลอง (เริ่มจากแถว header)
```

## โครงโค้ด `main.py`

แบ่งเป็น 4 ส่วนตามแนวคิดของวิชา:

```text
SENSE (read_sensor) → THINK (decide) → ACT (act) → LOG (log)
```

### วิธีใช้

1. copy โฟลเดอร์นี้ไปไว้ใน `submissions/team-XX/`
2. แก้ `read_sensor()` ใน `main.py` ให้ตรงกับ sensor ของทีม (ดูตัวอย่างใน `code-examples/04-dht`, `05-ldr`, `06-ultrasonic`)
3. แก้ threshold ทั้งสองค่า **จากข้อมูลจริง** + จดเหตุผลใน `system-diagram.md`
4. แก้ `act()` ให้ตรงกับ output ของทีม (LED / buzzer / web)
5. อยากมี dashboard? ผสมกับโค้ดใน [code-examples/08-wifi-webserver](../code-examples/08-wifi-webserver/)

### ทำไมต้องแยก function

- ทดสอบทีละส่วนได้: ลอง `decide(9999)` ใน REPL ดูว่าคืน ALERT จริงไหม โดยไม่ต้องสร้างเหตุการณ์จริง
- แบ่งงานในทีมได้: คนหนึ่งแก้ SENSE อีกคนแก้ ACT โดยไม่ชนกัน
- อ่าน flow ของระบบได้ใน 5 บรรทัดสุดท้าย

### เกณฑ์ขั้นต่ำที่ template นี้ครอบคลุม

- [x] sensor อย่างน้อย 1 ตัว
- [x] logic ตัดสินใจ (3 ระดับ)
- [x] output แจ้งเตือน
- [x] data logging ต่อเนื่อง (โบนัส)

## ใบงานที่รวมมาให้

- `problem-canvas.md` — สรุปปัญหา/ผู้ใช้/ไอเดียระบบ (จากครั้งที่ 1)
- `system-diagram.md` — block diagram, pin map, threshold (ครั้งที่ 8)
- `testing-table.md` — ตาราง test case (ครั้งที่ 9)
- `data.csv` — บันทึกผลจาก `main.py` (เปิดได้ด้วย Excel/Google Sheets)
