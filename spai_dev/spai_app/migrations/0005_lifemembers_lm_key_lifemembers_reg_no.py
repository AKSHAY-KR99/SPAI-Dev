# Generated by Django 5.0.6 on 2024-12-22 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spai_app', '0004_user_active_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='lifemembers',
            name='lm_key',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lifemembers',
            name='reg_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
