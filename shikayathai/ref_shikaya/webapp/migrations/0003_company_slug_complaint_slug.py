# Generated by Django 5.0 on 2024-02-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_complaint_image_complaint_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AddField(
            model_name='complaint',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
