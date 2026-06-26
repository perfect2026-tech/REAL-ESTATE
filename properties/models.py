from django.db import models
from agents.models import Agent

class Property(models.Model):
    PROPERTY_TYPES = [
        ('House', 'House'),
        ('Apartment', 'Apartment'),
        ('Land', 'Land'),
        ('Commercial', 'Commercial'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    location = models.CharField(max_length=100)
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES)
    bedrooms = models.PositiveIntegerField()
    bathrooms = models.PositiveIntegerField()
    area = models.FloatField()

    agent = models.ForeignKey(
        Agent,
        on_delete=models.CASCADE,
        related_name="properties"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title