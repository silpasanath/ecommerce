# Generated by Django 4.2.6 on 2023-10-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
