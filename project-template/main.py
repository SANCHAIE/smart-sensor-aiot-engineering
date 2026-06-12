# 09-final-project-template: โครงโค้ดสำหรับ Final Project
# โครงสร้าง: SENSE → THINK → ACT แยกเป็น function ชัดเจน
# ทีมแก้ 3 จุด: read_sensor(), decide(), act() ให้ตรงกับระบบของตัวเอง

from machine import ADC, Pin
import time

# ========== ตั้งค่าของทีม ==========
TEAM_NAME = "Team XX"
PROJECT_NAME = "Smart ______"

# threshold ต้องมาจาก data.csv ของทีม — เขียนเหตุผลใน README!
WARN_THRESHOLD = 2500
ALERT_THRESHOLD = 3200

LOG_FILE = "project_log.csv"
LOG_INTERVAL_S = 5

# ========== Hardware ==========
sensor = ADC(Pin(34))            # ← เปลี่ยนตาม sensor ของทีม
sensor.atten(ADC.ATTN_11DB)
led = Pin(5, Pin.OUT)
buzzer = Pin(18, Pin.OUT)


# ========== SENSE ==========
def read_sensor():
    """อ่านค่าเฉลี่ย 5 ครั้ง เพื่อลดค่าแกว่ง"""
    total = 0
    for _ in range(5):
        total += sensor.read()
        time.sleep(0.02)
    return total / 5


# ========== THINK ==========
def decide(value):
    """คืนสถานะ NORMAL / WARNING / ALERT จากค่า sensor"""
    if value >= ALERT_THRESHOLD:
        return "ALERT"
    elif value >= WARN_THRESHOLD:
        return "WARNING"
    return "NORMAL"


# ========== ACT ==========
def act(status):
    if status == "ALERT":
        led.on()
        buzzer.on()
    elif status == "WARNING":
        led.on()
        buzzer.off()
    else:
        led.off()
        buzzer.off()


# ========== LOG ==========
def log(t, value, status):
    with open(LOG_FILE, "a") as f:
        f.write("{},{},{}\n".format(t, value, status))


# ========== MAIN LOOP ==========
print("=== {} : {} ===".format(TEAM_NAME, PROJECT_NAME))
with open(LOG_FILE, "w") as f:
    f.write("time_s,value,status\n")

t = 0
while True:
    value = read_sensor()
    status = decide(value)
    act(status)
    log(t, value, status)
    print("t={}s value={:.0f} status={}".format(t, value, status))
    time.sleep(LOG_INTERVAL_S)
    t += LOG_INTERVAL_S
