# Generated by Django 4.0.1 on 2022-02-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loadImage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagetable',
            name='image',
            field=models.ImageField(blank=True, default='', upload_to='img/'),
        ),
    ]
