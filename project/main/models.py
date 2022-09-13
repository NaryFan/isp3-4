from django.db import models


class Categories(models.Model):
    objects = None
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category


class Dishes(models.Model):
    objects = None
    nameofdishes = models.CharField('Название', max_length=100, null=True)
    description = models.TextField()
    howTOcook = models.TextField()
    picture = models.ImageField(upload_to='images/')
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE)


def __str__(self):  #вывод объекта класса на экран
    return self.nameofdishes
