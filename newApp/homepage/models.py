from django.db import models

class Recipe(models.Model):
    Recipe_name = models.CharField(max_length=100)
    Recipe_description = models.TextField()
    Recipe_Ingrediants = models.TextField()
    Recipe_Image = models.ImageField(upload_to='images/')


# Create your models here.
