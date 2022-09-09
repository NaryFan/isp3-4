from django.db import models


class Task(models.Model):
    nameofdishes = models.CharField('Название', max_length=100) #название блюда
    task = models.TextField('Описание')

    def __str__(self): #вывод объекта класса на экран
        return self.nameofdishes

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'