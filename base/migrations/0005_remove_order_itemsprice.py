# Generated by Django 4.2.3 on 2023-07-18 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_order_itemsprice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='itemsPrice',
        ),
    ]
