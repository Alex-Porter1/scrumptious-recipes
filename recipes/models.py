from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=125)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.name + " by " + self.author

    description = models.TextField()
    image = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Step(models.Model):
    order = models.SmallIntegerField()
    directions = models.TextField()
    recipe = models.ForeignKey(
        "Recipe", related_name="steps", on_delete=models.CASCADE
    )
    food_items = models.ManyToManyField("FoodItem", blank=True)


class Measure(models.Model):
    name = models.CharField(max_length=30, unique=True)
    abbreviation = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100, null=True)
    amount = models.FloatField(null=True)

    def __str__(self):
        return self.name

    recipe = models.ForeignKey(
        "Recipe", related_name="ingredients", on_delete=models.CASCADE
    )
    measure = models.ForeignKey(
        "Measure", related_name="measures", on_delete=models.PROTECT
    )
    food = models.ForeignKey("FoodItem", on_delete=models.PROTECT)
