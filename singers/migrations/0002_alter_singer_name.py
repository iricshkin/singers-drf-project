# Generated by Django 4.1.7 on 2023-02-19 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('singers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='singer',
            name='name',
            field=models.CharField(max_length=70, unique=True, verbose_name='Исполнитель'),
        ),
    ]
