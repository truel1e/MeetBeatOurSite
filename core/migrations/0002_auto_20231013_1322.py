# Generated by Django 3.2.22 on 2023-10-13 10:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pan',
            name='vendor',
            field=models.CharField(choices=[('tefal', 'Tefal'), ('fissman', 'Fissman')], max_length=128),
        ),
        migrations.AlterField(
            model_name='potato',
            name='country',
            field=models.CharField(choices=[('bel', 'Беларусь'), ('rus', 'Россия')], max_length=128),
        ),
        migrations.AlterField(
            model_name='potato',
            name='id',
            field=models.CharField(default=uuid.UUID('d088c628-f953-4d47-9dcc-59faef5307f2'), max_length=128, primary_key=True, serialize=False),
        ),
    ]
