# 07 — Data Logger + Analysis

| ไฟล์ | รันที่ไหน | คำอธิบาย |
|---|---|---|
| `main.py` | ESP32 | เก็บค่า sensor 60 จุดลง `data.csv` |
| `analyze.py` | คอมพิวเตอร์ | หา min/max/average + plot กราฟ + moving average |

## ขั้นตอนใช้งาน

1. แก้ `read_sensor()` ใน `main.py` ให้ตรงกับ sensor ของทีม
2. รันบน ESP32 จนขึ้น `Done!`
3. ดึงไฟล์: Thonny → `View → Files` → คลิกขวา `data.csv` → Download
4. รัน `analyze.py` บนคอม (ต้องมี `pip install matplotlib`) หรือเปิด CSV ใน Google Sheets

## จุดสอน

- ข้อมูลที่ "บันทึกไว้" วิเคราะห์ย้อนหลังได้ — ต่างจากการดูค่าสด ๆ ผ่าน REPL
- threshold ที่ดีมาจากการดูกราฟข้อมูลจริง ไม่ใช่การเดา
- moving average ทำให้เส้นนิ่งขึ้น แต่ตอบสนองช้าลง — trade-off ที่วิศวกรต้องเลือก
