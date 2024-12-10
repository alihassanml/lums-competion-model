from ultralytics import YOLO

# this file purpose to test model on single images
model = YOLO('best.pt')

results = model.predict('096.JPG')
results[0].show()