# Generated by Django 4.2.4 on 2023-10-18 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('founde', '0005_item_image1_item_image2'),
    ]

    operations = [
        migrations.AddField(
            model_name='mycustomusers',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]