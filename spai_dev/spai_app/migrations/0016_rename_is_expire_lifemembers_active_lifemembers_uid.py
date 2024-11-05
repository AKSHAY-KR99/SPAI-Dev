# Generated by Django 5.0.6 on 2024-11-05 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spai_app', '0015_lifemembers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lifemembers',
            old_name='is_expire',
            new_name='active',
        ),
        migrations.AddField(
            model_name='lifemembers',
            name='uid',
            field=models.SlugField(auto_created=True, blank=True, null=True, unique=True),
        ),
    ]
