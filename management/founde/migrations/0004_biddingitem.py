# Generated by Django 4.2.4 on 2023-10-17 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('founde', '0003_bid'),
    ]

    operations = [
        migrations.CreateModel(
            name='BiddingItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid_id', models.CharField(max_length=20)),
                ('product_description', models.CharField(max_length=100)),
                ('bid_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]