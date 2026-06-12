# ครั้งที่ 7: Wi-Fi / Web Dashboard

> **เป้าหมาย:** ทำให้ระบบเป็น IoT จริง — ดูค่า sensor ผ่านมือถือ/คอมได้

## โครงเวลา (120 นาที)

| ช่วง | เวลา | กิจกรรม |
|---|---|---|
| 1 | 25 นาที | concept client-server แบบง่าย + demo เปิดหน้า web จาก ESP32 |
| 2 | 65 นาที | เชื่อม Wi-Fi → web server แสดงค่า sensor → เปิดจากมือถือ |
| 3 | 20 นาที | **Team Challenge: Dashboard เปลี่ยนสีตามสถานะ** + log |
| 4 | 10 นาที | สรุป + exit ticket |

## Concept หลัก

```text
มือถือ (client) ──ขอหน้าเว็บ──▶ ESP32 (server)
มือถือ (client) ◀──ส่ง HTML──── ESP32 (server)
```

ESP32 เป็นได้ทั้ง "เว็บเซิร์ฟเวอร์จิ๋ว" — ใครอยู่ Wi-Fi วงเดียวกันเปิดดูได้

## ขั้นตอน

ดูโค้ดเต็มที่ [`code-examples/08-wifi-webserver/`](../code-examples/08-wifi-webserver/)

### 1. เชื่อม Wi-Fi

```python
import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("ชื่อWiFi", "รหัสผ่าน")

while not wlan.isconnected():
    pass
print("Connected! IP:", wlan.ifconfig()[0])
```

### 2. Web server แสดงค่า sensor

```python
import socket

def web_page(value, status):
    return """<html><head><meta http-equiv="refresh" content="2"></head>
    <body style="font-family:sans-serif;text-align:center">
    <h1>Team 01 Sensor Dashboard</h1>
    <h2>Value: {}</h2>
    <h2>Status: {}</h2>
    </body></html>""".format(value, status)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("", 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    conn.recv(1024)
    value = ldr.read()
    status = "ALERT" if value > THRESHOLD else "NORMAL"
    conn.send("HTTP/1.1 200 OK\nContent-Type: text/html\n\n")
    conn.sendall(web_page(value, status))
    conn.close()
```

3. เปิดเบราว์เซอร์ในมือถือ → พิมพ์ IP ของ ESP32 → เห็นค่า sensor สด ๆ

## ⚠️ แผนสำรอง (ถ้า Wi-Fi โรงเรียนมีปัญหา)

- ใช้ hotspot จากมือถือครู (ESP32 ใช้ได้เฉพาะ Wi-Fi 2.4GHz)
- หรือเปลี่ยนเป็น **Serial Dashboard**: print ค่าแบบจัด format สวย ๆ + แถบสถานะใน REPL
- หรือต่อจอ OLED แสดงค่าแทน

## 🏆 Team Challenge: "Dashboard เปลี่ยนสีตามสถานะ"

อัปเกรดหน้า web ให้:
- พื้นหลัง **เขียว** เมื่อ NORMAL, **เหลือง** เมื่อ WARNING, **แดง** เมื่อ ALERT (ใช้ 3 ระดับจากครั้งที่แล้ว)
- refresh อัตโนมัติทุก 2 วินาที
- มีชื่อทีมและชื่อระบบบนหน้า web

ใบ้: เปลี่ยน `style="background:{}"` ตามตัวแปร status

ทีมแรกที่เปิดจากมือถือสมาชิกครบ 3 เครื่องพร้อมกันและสีเปลี่ยนตามจริง = ชนะ

## ชิ้นงานที่ต้องส่ง

- [ ] หน้า web/dashboard แสดงค่า sensor ได้ (ครูเช็คจากมือถือครูเอง)
- [ ] screenshot หน้า dashboard ลง `submissions/team-XX/`
- [ ] log 5 บรรทัด

## Exit Ticket

"ถ้าอยากดูค่าจากบ้าน (คนละ Wi-Fi) ต้องใช้อะไรเพิ่ม" (ปูทาง cloud/MQTT สำหรับคนที่อยากไปต่อ)

## ✨ Bonus Challenge

ส่งข้อมูลขึ้น **Google Sheets** ผ่าน Apps Script Web App หรือแสดง**ค่าย้อนหลัง 10 ค่าล่าสุด**เป็นตารางบนหน้า web
