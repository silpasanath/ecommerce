# Generated by Django 4.2.6 on 2023-11-02 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0012_alter_todos_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='customermodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('product_name', models.CharField(max_length=100)),
                ('delivered_date', models.DateField()),
            ],
        ),
    ]
