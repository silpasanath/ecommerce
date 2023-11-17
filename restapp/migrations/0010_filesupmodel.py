# Generated by Django 4.2.6 on 2023-10-30 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0009_employeemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='filesupmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='pdf/')),
                ('audiofile', models.FileField(upload_to='audio/')),
                ('videofile', models.FileField(upload_to='video/')),
            ],
        ),
    ]
