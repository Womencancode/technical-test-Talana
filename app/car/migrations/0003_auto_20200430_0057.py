# Generated by Django 2.2.10 on 2020-04-30 00:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20200430_0055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='number_of_doors',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(5)]),
        ),
    ]
