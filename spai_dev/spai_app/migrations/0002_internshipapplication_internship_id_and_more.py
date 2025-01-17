# Generated by Django 5.0.6 on 2024-12-16 19:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spai_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='internshipapplication',
            name='internship_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='approval_percentage',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AddField(
            model_name='user',
            name='executive',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
