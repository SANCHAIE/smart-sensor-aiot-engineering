# ครั้งที่ 5: Data Logging + Data Visualization

> **เป้าหมาย:** เก็บข้อมูล sensor เป็นไฟล์ วิเคราะห์ และหา threshold จากข้อมูลจริง (ต่อยอด Python/Data Science ปีที่แล้ว)

## โครงเวลา (120 นาที)

| ช่วง | เวลา | กิจกรรม |
|---|---|---|
| 1 | 20 นาที | ทำไมต้อง log ข้อมูล + demo เปิด CSV plot กราฟ |
| 2 | 70 นาที | เก็บข้อมูลเป็น CSV → เปิดใน Python/Google Sheets → plot กราฟ → หา min/max/average |
| 3 | 20 นาที | **Team Challenge: ตามล่าค่าผิดปกติ** + log |
| 4 | 10 นาที | แชร์ insight ทีมละ 1 ข้อ + exit ticket |

## ขั้นตอน

### 1. เก็บข้อมูลเป็น CSV บน ESP32

ดูโค้ดเต็มที่ [`code-examples/07-data-logger/`](../code-examples/07-data-logger/)

```python
from machine import ADC, Pin
import time

ldr = ADC(Pin(34))
ldr.atten(ADC.ATTN_11DB)

with open("data.csv", "w") as f:
    f.write("time_s,light\n")
    for i in range(60):              # เก็บ 60 จุด ทุก 2 วินาที = 2 นาที
        value = ldr.read()
        f.write("{},{}\n".format(i * 2, value))
        print(i * 2, value)
        time.sleep(2)

print("Done! saved to data.csv")
```

ดึงไฟล์ออกจากบอร์ดผ่าน Thonny: `View → Files` → คลิกขวา `data.csv` → Download

### 2. วิเคราะห์บนคอมพิวเตอร์

เปิดใน Google Sheets **หรือ** ใช้ Python:

```python
import csv

values = []
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        values.append(int(row["light"]))

print("min:", min(values))
print("max:", max(values))
print("average:", sum(values) / len(values))
```

### 3. Plot กราฟ (matplotlib หรือ Sheets)

```python
import matplotlib.pyplot as plt
plt.plot(values)
plt.xlabel("sample")
plt.ylabel("light")
plt.title("Team 01 - Light Sensor Data")
plt.savefig("graph.png")
```

### 4. หา threshold เบื้องต้น

จากกราฟ: ค่าช่วง "ปกติ" อยู่แถวไหน ค่าช่วง "ผิดปกติ" อยู่แถวไหน → ขีดเส้น threshold แล้วจดเหตุผลไว้

## 🏆 Team Challenge: "ตามล่าค่าผิดปกติ"

1. แต่ละทีมเก็บข้อมูล 60 จุด โดย **แอบสร้างเหตุการณ์ผิดปกติ 2 ช่วง** (เช่น เอามือบัง, เป่าลมร้อน) โดยจดเวลาไว้ลับ ๆ
2. ส่งไฟล์ CSV ให้ทีมข้าง ๆ (ผ่าน GitHub หรือ USB)
3. ทีมที่ได้รับต้อง plot กราฟแล้ว **ชี้ให้ได้ว่าเหตุการณ์ผิดปกติเกิดวินาทีที่เท่าไร**

ทีมที่หาเจอครบและแม่นที่สุดชนะ — นี่คือ anomaly detection แบบมือเปล่า!

## ชิ้นงานที่ต้องส่ง

- [ ] `data.csv` (อย่างน้อย 60 แถว) อัปโหลดลง `teams/team-XX/data/`
- [ ] กราฟอย่างน้อย 1 รูป
- [ ] **insight 3 ข้อ** จากข้อมูล (เช่น ค่าปกติ, ค่าแกว่ง, threshold ที่เลือกและเหตุผล)
- [ ] log 5 บรรทัด

## Exit Ticket

"threshold ของทีมเราคือเท่าไร และทำไมถึงเลือกค่านั้น"

## ✨ Bonus Challenge

คำนวณ **moving average** (เฉลี่ยทีละ 5 จุด) แล้ว plot เทียบกับข้อมูลดิบ — เส้นไหนใช้ตัดสินใจได้ดีกว่า เพราะอะไร
