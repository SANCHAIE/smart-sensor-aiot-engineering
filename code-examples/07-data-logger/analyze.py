# analyze.py — รันบน "คอมพิวเตอร์" (ไม่ใช่บน ESP32) หลังดึง data.csv มาแล้ว
# วิเคราะห์ min/max/average + plot กราฟ + ขีดเส้น threshold

import csv

import matplotlib.pyplot as plt

times = []
values = []
with open("data.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        times.append(int(row["time_s"]))
        values.append(int(row["value"]))

print("samples:", len(values))
print("min:", min(values))
print("max:", max(values))
print("average:", sum(values) / len(values))

# moving average ทีละ 5 จุด (Bonus Challenge ครั้งที่ 5)
window = 5
smooth = [sum(values[i:i + window]) / window for i in range(len(values) - window + 1)]

THRESHOLD = 3000   # ← แก้เป็นค่าของทีมเอง พร้อมเหตุผล

plt.plot(times, values, label="raw")
plt.plot(times[window - 1:], smooth, label="moving avg (5)")
plt.axhline(THRESHOLD, color="red", linestyle="--", label="threshold")
plt.xlabel("time (s)")
plt.ylabel("sensor value")
plt.title("Team XX - Sensor Data")
plt.legend()
plt.savefig("graph.png", dpi=150)
plt.show()
