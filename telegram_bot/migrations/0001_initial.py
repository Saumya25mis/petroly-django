# Generated by Django 4.0.6 on 2022-07-22 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramProfile',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='telegram user ID')),
                ('chat_id', models.IntegerField(unique=True, verbose_name='chat ID')),
                ('username', models.CharField(max_length=256, unique=True, verbose_name='telegram username')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
