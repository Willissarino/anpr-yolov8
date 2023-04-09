from ultralytics import YOLO

# Load a model
model = YOLO('yolo-model/anpr_v8.pt')  # load an official model

# Export the model to TensorRT
model.export(format='engine', device='0')
