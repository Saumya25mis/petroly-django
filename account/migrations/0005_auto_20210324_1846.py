# Generated by Django 3.1.7 on 2021-03-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210227_0509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(choices=[('ICS', 'ICS'), ('PHYS', 'PHYS'), ('COE', 'COE'), ('SWE', 'SWE'), ('ACCT', 'ACCT'), ('AE', 'AE'), ('ME', 'ME'), ('ENGL', 'ENGL'), ('IAS', 'IAS'), ('EE', 'CC'), ('CHEM', 'CHEM')], default='', max_length=25),
        ),
    ]
