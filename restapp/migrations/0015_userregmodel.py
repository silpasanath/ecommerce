# Generated by Django 4.2.6 on 2023-11-02 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0014_delete_customermodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='userregmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]