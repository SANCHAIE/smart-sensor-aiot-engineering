# 03-buzzer: เสียงเตือน + เล่นโน้ตด้วย PWM
# วงจร: GPIO 18 → buzzer (+) ... (−) → GND
# active buzzer: แค่ on/off ก็ดัง | passive buzzer: ต้องใช้ PWM กำหนดความถี่

from machine import Pin, PWM
import time

# ---- แบบที่ 1: active buzzer (on/off ธรรมดา) ----
buzzer = Pin(18, Pin.OUT)

for _ in range(3):
    buzzer.on()
    time.sleep(0.2)
    buzzer.off()
    time.sleep(0.2)

time.sleep(1)

# ---- แบบที่ 2: passive buzzer เล่นโน้ตด้วย PWM ----
NOTES = {"C": 262, "D": 294, "E": 330, "F": 349, "G": 392, "A": 440, "B": 494}

pwm = PWM(Pin(18), freq=440, duty=0)


def play(note, duration=0.3):
    pwm.freq(NOTES[note])
    pwm.duty(512)          # ความดัง 50%
    time.sleep(duration)
    pwm.duty(0)            # เงียบ
    time.sleep(0.05)


for note in ["C", "D", "E", "F", "G", "A", "B"]:
    play(note)

pwm.deinit()
