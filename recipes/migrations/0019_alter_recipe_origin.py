# Generated by Django 4.0.3 on 2022-06-03 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0018_alter_recipe_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='origin',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
