from django.db import models

# Create your models here.

class Recipes(models.Model):
    Recipe_name = models.CharField(max_length=100)
    Recipe_description = models.TextField()
    Recipe_Image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.Recipe_name