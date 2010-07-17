from django.db import models

# Create your models here.

class Squares(models.Model):

    colors = models.CharField(max_length = 30)

    def render(self):
        return self.colors

    def __str__(self):
        return self.colors

    def rotate(self):
        self.colors = self.colors[1:] + self.colors[0]
