# Generated by Django 4.2.4 on 2023-10-19 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('founde', '0007_remove_item_sing_remove_postnews_sing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='founditem',
            name='sing',
        ),
        migrations.RemoveField(
            model_name='lostitem1',
            name='sing',
        ),
    ]
