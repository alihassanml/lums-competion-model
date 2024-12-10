from ultralytics import YOLO

model = YOLO('best.pt')

results = model.predict('test_data/096.JPG')
results[0].show()