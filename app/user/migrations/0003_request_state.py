# Generated by Django 2.2.10 on 2020-04-30 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200430_0124'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='state',
            field=models.CharField(blank=True, choices=[('PE', 'Pendiente'), ('AD', 'Aprobado'), ('RE', 'Rechazado')], default='PE', max_length=2),
        ),
    ]
