# Generated by Django 4.0.3 on 2022-06-03 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0022_remove_recipe_origin_alter_ingredient_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='food_items',
            field=models.ManyToManyField(to='recipes.fooditem'),
        ),
    ]