# Generated by Django 4.2.6 on 2023-11-02 18:00

from django.db import migrations, models
import restapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0016_customermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customermodel',
            name='delivered_date',
            field=models.DateField(validators=[restapp.models.datefun]),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='name',
            field=models.CharField(max_length=10, validators=[restapp.models.unamefun]),
        ),
        migrations.AlterField(
            model_name='customermodel',
            name='product_name',
            field=models.CharField(max_length=100, validators=[restapp.models.productname]),
        ),
    ]
