# Generated by Django 4.0.6 on 2022-08-20 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0006_alter_cache_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cache',
            name='updated_on',
            field=models.DateTimeField(verbose_name='updated on'),
        ),
    ]
