# Generated by Django 4.0.5 on 2022-08-16 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('john', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='greetings_1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='home',
            name='greetings_2',
            field=models.CharField(max_length=10),
        ),
    ]
