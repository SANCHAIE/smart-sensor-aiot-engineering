# แผนสำรอง: Serial Dashboard — ใช้เมื่อ Wi-Fi โรงเรียนมีปัญหา
# แสดงแถบค่าและสถานะใน console ของ Thonny แทนหน้า web

from machine import ADC, Pin
import time

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

WARN_THRESHOLD = 2500
ALERT_THRESHOLD = 3200
MAX_VALUE = 4095
BAR_WIDTH = 40

while True:
    value = ldr.read()
    filled = int(value / MAX_VALUE * BAR_WIDTH)
    bar = "#" * filled + "-" * (BAR_WIDTH - filled)

    if value >= ALERT_THRESHOLD:
        status = "!!! ALERT !!!"
    elif value >= WARN_THRESHOLD:
        status = "  WARNING"
    else:
        status = "  normal"

    print("[{}] {:4d} {}".format(bar, value, status))
    time.sleep(0.5)
