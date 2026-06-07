from django.conf import settings
import os
from ultralytics import YOLO

# model_path = os.path.join(
#     settings.BASE_DIR,
#     'static',
#     'ocrresources',
#     'best.pt'
# )

# model = YOLO(model_path)

# def get_classes():
#     print(model.names)
#     return model.names