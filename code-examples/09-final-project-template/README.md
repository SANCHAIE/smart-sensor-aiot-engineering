# 09 — Final Project Template

โครงโค้ดเริ่มต้นสำหรับ final project — แบ่งเป็น 4 ส่วนตามแนวคิดของวิชา:

```text
SENSE (read_sensor) → THINK (decide) → ACT (act) → LOG (log)
```

## วิธีใช้

1. copy `main.py` ไปไว้ใน `teams/team-XX/code/`
2. แก้ `read_sensor()` ให้ตรงกับ sensor ของทีม (ดูตัวอย่างใน 04/05/06)
3. แก้ threshold ทั้งสองค่า **จากข้อมูลจริง** + จดเหตุผลใน README ทีม
4. แก้ `act()` ให้ตรงกับ output ของทีม (LED / buzzer / web)
5. อยากมี dashboard? ผสมกับโค้ดใน [08-wifi-webserver](../08-wifi-webserver/)

## ทำไมต้องแยก function

- ทดสอบทีละส่วนได้: ลอง `decide(9999)` ใน REPL ดูว่าคืน ALERT จริงไหม โดยไม่ต้องสร้างเหตุการณ์จริง
- แบ่งงานในทีมได้: คนหนึ่งแก้ SENSE อีกคนแก้ ACT โดยไม่ชนกัน
- อ่าน flow ของระบบได้ใน 5 บรรทัดสุดท้าย

## เกณฑ์ขั้นต่ำที่ template นี้ครอบคลุม

- [x] sensor อย่างน้อย 1 ตัว
- [x] logic ตัดสินใจ (3 ระดับ)
- [x] output แจ้งเตือน
- [x] data logging ต่อเนื่อง (โบนัส)
