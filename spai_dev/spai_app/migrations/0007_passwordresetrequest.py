# Generated by Django 5.1.4 on 2024-12-25 07:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spai_app', '0006_eventdocumentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PasswordResetRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='password_reset', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
