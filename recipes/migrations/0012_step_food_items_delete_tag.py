# Generated by Django 4.0.3 on 2022-06-02 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='food_items',
            field=models.ManyToManyField(blank=True, null=True, to='recipes.fooditem'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
