# Generated by Django 2.2.10 on 2020-04-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('SE', 'Sedán'), ('SU', 'SUV'), ('CO', 'Coupé'), ('HA', 'Hatchback'), ('PI', 'Pick-up'), ('SW', 'Station Wagon'), ('OT', 'Otro')], max_length=2),
        ),
    ]