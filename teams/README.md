# Teams — พื้นที่ผลงานของแต่ละทีม

แต่ละทีมมีโฟลเดอร์ของตัวเอง (`team-01/` ถึง `team-10/`) ใช้เป็น **portfolio ของทีม** ตลอดคอร์ส

## โครงสร้างที่แนะนำในโฟลเดอร์ทีม

```text
team-XX/
├── README.md          ← หน้าหลักของทีม + log รายสัปดาห์
├── problem-canvas.md  ← copy จาก worksheets แล้วเติม
├── code/              ← โค้ดของทีม (อัปเดตทุกครั้งที่มีของใหม่)
├── data/              ← data.csv + กราฟ
├── images/            ← รูปวงจร, system diagram, screenshot dashboard
├── testing-table.md   ← copy จาก worksheets แล้วเติม
└── presentation/      ← slide/poster สำหรับ Demo Day
```

## กติกา log รายสัปดาห์

ทุกครั้งก่อนหมดคาบ เติมใน README ของทีมอย่างน้อย 5 บรรทัด:

```text
วันนี้ทำอะไร
ต่อวงจรอะไร
โค้ดสำคัญคืออะไร
เจอปัญหาอะไร
ครั้งหน้าจะทำอะไรต่อ
```

## วิธีอัปโหลดงาน (ไม่ต้องใช้ Git command)

1. เข้า GitHub repo ผ่านเบราว์เซอร์ → ไปที่โฟลเดอร์ทีมตัวเอง
2. ปุ่ม `Add file → Upload files` สำหรับรูป/ไฟล์ หรือ `Edit` (ไอคอนดินสอ) สำหรับแก้ README
3. เขียนข้อความ commit สั้น ๆ ว่าเพิ่มอะไร → `Commit changes`

ทีมไหนอยากใช้ Git จริง (clone/commit/push) ถามครูได้ — มีดาวพิเศษให้ ⭐
