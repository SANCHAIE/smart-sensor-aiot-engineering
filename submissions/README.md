# Submissions — พื้นที่ส่งงานของแต่ละทีม

แต่ละทีมมีโฟลเดอร์ของตัวเอง (`team-01/` ถึง `team-10/`) ใช้เป็น **portfolio ของทีม** ตลอดคอร์ส

## กติกาการส่งงาน (ระบบ Fork)

1. แต่ละทีมต้อง **Fork repo นี้** ไปยังบัญชี GitHub ของตัวแทนทีม (GitHub Manager)
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

## โครงสร้างที่แนะนำในโฟลเดอร์ทีม

```text
team-XX/
├── README.md          ← หน้าหลักของทีม + log รายสัปดาห์
├── problem-canvas.md  ← copy จาก worksheets/stem-problem-canvas.md แล้วเติม
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

## วิธีทำงานใน fork ของทีม (ไม่ต้องใช้ Git command)

1. ตัวแทนทีมกดปุ่ม **Fork** มุมขวาบนของ repo กลาง (ทำครั้งเดียวตอนเริ่มคอร์ส)
2. เข้า **fork ของทีม** ผ่านเบราว์เซอร์ → ไปที่โฟลเดอร์ `submissions/team-XX/` ของตัวเอง
3. ปุ่ม `Add file → Upload files` สำหรับรูป/ไฟล์ หรือ `Edit` (ไอคอนดินสอ) สำหรับแก้ README
4. เขียนข้อความ commit สั้น ๆ ว่าเพิ่มอะไร → `Commit changes`
5. เมื่อต้องส่งงาน: ส่ง link fork ผ่าน Google Form หรือกด `Contribute → Open pull request` กลับมายัง repo กลาง

ทีมไหนอยากใช้ Git จริง (clone/commit/push) ถามครูได้ — มีดาวพิเศษให้ ⭐
