# Generated by Django 4.2.4 on 2023-10-18 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('founde', '0006_mycustomusers_is_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='sing',
        ),
        migrations.RemoveField(
            model_name='postnews',
            name='sing',
        ),
    ]
