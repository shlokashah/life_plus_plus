# Generated by Django 2.2.2 on 2019-08-18 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prescription', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prescriptions',
            name='image',
            field=models.ImageField(blank=True, default='documents/ghi.jpeg', upload_to='documents/'),
        ),
    ]
