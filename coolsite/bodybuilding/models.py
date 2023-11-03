from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Exercise(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    about = models.TextField(blank=True, verbose_name="Описание")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL", unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('exercise', kwargs={'exerciseSlug': self.slug})


class Muscle(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    about = models.TextField(blank=True, verbose_name="Описание")
    exercises = models.ManyToManyField(Exercise)
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL", unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('muscle', kwargs={'muscleSlug': self.slug})


class Relation(models.Model):
    parent = models.ForeignKey(Muscle, on_delete=models.CASCADE, related_name='child', blank=True)
    child = models.ForeignKey(Muscle, on_delete=models.CASCADE, related_name='parent', blank=True)


class Recipe(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    nutrients = models.CharField(max_length=50, verbose_name="Макронутриенты")
    ingredients = models.TextField(blank=True, verbose_name="Ингридиенты")
    cooking = models.TextField(blank=True, verbose_name="Готовка")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL", unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe', kwargs={'recipeSlug': self.slug})


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
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="URL", unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('sportNutrition', kwargs={'sportNutritionSlug': self.slug})


class CalorieCount(models.Model):
    calorie = models.IntegerField(verbose_name="Калории")
    protein = models.IntegerField(verbose_name="Белки")
    fat = models.IntegerField(verbose_name="Жиры")
    carbs = models.IntegerField(verbose_name="Углеводы")
    date = models.DateField(verbose_name="Дата")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', blank=True)
