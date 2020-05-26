from django.db import models

# Create your models here.
# models定義後はmigrationを忘れずに


class Product(models.Model):
    # CharFieldを使う際はmax_lengthは必ず必要
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')

    def __str__(self):
        return self.name
