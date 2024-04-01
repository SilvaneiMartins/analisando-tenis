from ultralytics import YOLO

model = YOLO("yolov8x")  # Carregando o modelo YOLOv5x

model.predict("input_videos/image.png", save=True)  # Realizando a predição da imagem
