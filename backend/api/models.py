from django.db import models

# Create your models here.
class Painting(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    image = models.ImageField(upload_to='paintings/')
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title