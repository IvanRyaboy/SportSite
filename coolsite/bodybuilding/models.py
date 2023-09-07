from django.db import models


class Muscle(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    about = models.TextField(blank=True, verbose_name="Описание")


class Relation(models.Model):
    parent = models.ForeignKey(Muscle, on_delete=models.CASCADE, related_name='child', blank=True)
    child = models.ForeignKey(Muscle, on_delete=models.CASCADE, related_name='parent', blank=True)