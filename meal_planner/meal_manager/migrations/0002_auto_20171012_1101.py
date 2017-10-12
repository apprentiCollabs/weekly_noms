# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-12 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal_manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(blank=True, related_name='recipes', to='meal_manager.Ingredient'),
        ),
    ]