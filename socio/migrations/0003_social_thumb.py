# Generated by Django 2.1.1 on 2018-10-03 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socio', '0002_auto_20181002_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='social',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
    ]
