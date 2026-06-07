from django.db import models
from django.forms.models import ModelForm



class ResAiModel(models.Model):
    name = models.CharField(max_length=50)
    yolo_model = models.FileField(upload_to='ocrresources/')

    def __str__(self):
        return self.name


    

