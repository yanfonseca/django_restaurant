# Generated by Django 2.2.6 on 2020-12-10 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_recipe_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='publish',
            field=models.BooleanField(default=False),
        ),
    ]
