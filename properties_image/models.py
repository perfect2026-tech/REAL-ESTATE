from django.db import models
from properties.models import Property

# Create your models here.

class PropertyImage(models.Model):
    property = models.ForeignKey(
        Property,
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(upload_to="properties/")

    def __str__(self):
        return f"Image for {self.property.title}"