# Generated by Django 4.2.1 on 2023-07-27 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='projects'),
        ),
    ]
