# 08 — Wi-Fi Web Dashboard

| ไฟล์ | คำอธิบาย |
|---|---|
| `main.py` | Web server แสดงค่า sensor + พื้นหลังเปลี่ยนสีตามสถานะ 3 ระดับ |
| `serial_dashboard.py` | แผนสำรองถ้า Wi-Fi ใช้ไม่ได้ — dashboard ใน console |

## วิธีใช้

1. แก้ `WIFI_SSID` / `WIFI_PASSWORD` (⚠️ ESP32 ต่อได้เฉพาะ Wi-Fi **2.4GHz**)
2. แก้ threshold ทั้งสองค่าให้มาจากข้อมูลจริงของทีม
3. รัน → ดู IP ใน console → เปิดเบราว์เซอร์มือถือ (วง Wi-Fi เดียวกัน) พิมพ์ IP นั้น

## จุดสอน

- client-server: มือถือ "ขอ" หน้าเว็บ, ESP32 "ตอบ" ด้วย HTML
- `<meta http-equiv="refresh" content="2">` = ให้เบราว์เซอร์ขอใหม่ทุก 2 วินาที (polling แบบง่ายสุด)
- ⚠️ อย่า commit รหัสผ่าน Wi-Fi จริงขึ้น GitHub — ใช้คำว่า `รหัสผ่าน` แทนก่อน push

## แก้ปัญหาที่พบบ่อย

| อาการ | ทางแก้ |
|---|---|
| ต่อ Wi-Fi ไม่ติด | เช็คว่าเป็น 2.4GHz, ลอง hotspot มือถือ |
| เปิดหน้า web ไม่ขึ้น | มือถือต้องอยู่ Wi-Fi วงเดียวกับ ESP32 |
| `OSError: [Errno 98]` | บอร์ดยังเปิด socket เก่าค้าง → กดปุ่ม RST รีเซ็ตบอร์ด |
