from django.db import models
from django.urls import reverse


class Exercise(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    about = models.TextField(blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exercise', kwargs={'exercise_id': self.pk})


class Muscle(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    about = models.TextField(blank=True, verbose_name="Описание")
    exercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('muscle', kwargs={'muscle_id': self.pk})


class Relation(models.Model):
    parent = models.ForeignKey(Muscle, on_delete=models.CASCADE, related_name='child', blank=True)
    child = models.ForeignKey(Muscle, on_delete=models.CASCADE, related_name='parent', blank=True)


class Recipe(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    nutrients = models.CharField(max_length=50, verbose_name="Макронутриенты")
    ingredients = models.TextField(blank=True, verbose_name="Ингридиенты")
    cooking = models.TextField(blank=True, verbose_name="Готовка")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'recipe_id': self.pk})


class SportNutrition(models.Model):
    S = "S"
    A = "A"
    B = "B"
    C = "C"
    TierList = [
        (S, "Богоподобно"),
        (A, "Отлично"),
        (B, "Есть но"),
        (C, "Зачем")
    ]
    name = models.CharField(max_length=50, verbose_name="Название")
    about = models.TextField(blank=True, verbose_name="Описание")
    tierList = models.CharField(max_length=1, choices=TierList, default=S)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sportNutrition', kwargs={'sportNutrition_id': self.pk})
