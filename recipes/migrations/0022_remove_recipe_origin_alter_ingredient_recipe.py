# Generated by Django 4.0.3 on 2022-06-03 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0021_alter_ingredient_recipe'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='origin',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='recipes.recipe'),
        ),
    ]
