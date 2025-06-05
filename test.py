from ultralytics import YOLO
from pathlib import Path

model = YOLO("best.pt")

results = model(r"C:\Users\fabian.escobar\Desktop\Universidad\Proyecto Cherry\dataset\test\images\cherry_N00451_2021_12_21_H08_50_ripe_fruits_visit2_plot1_row_10_01.JPG", conf=0.25, save=True)

img_dir = Path("data/pruebas")
for img in img_dir.glob("*.jpg"):
    results = model(img, save=True)

for r in results:
    for box in r.boxes:
        cls = int(box.cls)         
        conf = float(box.conf)
        x1, y1, x2, y2 = box.xyxy[0] 

