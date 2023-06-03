from django.db import models

class Category(models.Model):
    name_tm = models.CharField(max_length=255)
    name_ru = models.CharField(max_length=255)

    def __str__(self):
        return self.name_ru
    
    class Meta:
        verbose_name_plural = 'Категории'
