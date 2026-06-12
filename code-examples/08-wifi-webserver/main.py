# 08-wifi-webserver: แสดงค่า sensor ผ่านหน้า web (ESP32 เป็น server)
# ใช้กับครั้งที่ 7 — เปิดเบราว์เซอร์ในวง Wi-Fi เดียวกัน พิมพ์ IP ที่ขึ้นใน console

from machine import ADC, Pin
import network
import socket
import time

# ---------- ตั้งค่า ----------
WIFI_SSID = "ชื่อWiFi"          # ← แก้ตรงนี้ (ESP32 ใช้ได้เฉพาะ 2.4GHz)
WIFI_PASSWORD = "รหัสผ่าน"      # ← แก้ตรงนี้
TEAM_NAME = "Team 01"
WARN_THRESHOLD = 2500           # ← จากข้อมูลจริงของทีม
ALERT_THRESHOLD = 3200          # ← จากข้อมูลจริงของทีม

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

# ---------- เชื่อม Wi-Fi ----------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)
print("Connecting to Wi-Fi", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(0.5)
print("\nConnected! เปิดเบราว์เซอร์ไปที่: http://{}".format(wlan.ifconfig()[0]))


# ---------- สถานะ 3 ระดับ (Challenge ครั้งที่ 7) ----------
def get_status(value):
    if value >= ALERT_THRESHOLD:
        return "ALERT", "#e74c3c"      # แดง
    elif value >= WARN_THRESHOLD:
        return "WARNING", "#f1c40f"    # เหลือง
    return "NORMAL", "#2ecc71"         # เขียว


def web_page(value, status, color):
    return """<!DOCTYPE html>
<html><head>
<meta charset="utf-8">
<meta http-equiv="refresh" content="2">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{team} Dashboard</title>
</head>
<body style="background:{color};font-family:sans-serif;text-align:center;color:#fff">
<h1>{team} Sensor Dashboard</h1>
<p style="font-size:5em;margin:0">{value}</p>
<h2>Status: {status}</h2>
</body></html>""".format(team=TEAM_NAME, color=color, value=value, status=status)


# ---------- Web server ----------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("", 80))
s.listen(5)

while True:
    conn, addr = s.accept()
    try:
        conn.recv(1024)
        value = ldr.read()
        status, color = get_status(value)
        conn.send("HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n")
        conn.sendall(web_page(value, status, color))
    finally:
        conn.close()
