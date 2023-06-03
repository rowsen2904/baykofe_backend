from django.db import models

from category.models import Category 

def upload_to(instance, filename):
    return 'products/{filename}'.format(filename=filename)

class Product(models.Model):
    @property
    def image_url(self):
        if self.img and hasattr(self.img, 'url'):
            return self.img.url

    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    price = models.PositiveSmallIntegerField()
    ready_time = models.PositiveSmallIntegerField()
    img = models.FileField(upload_to=upload_to, 
                            default="default.png")

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Продукты'