# Generated by Django 4.2.3 on 2023-07-20 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_order_itemsprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='image',
            field=models.CharField(blank=True, default='/placeholder.png', max_length=200, null=True),
        ),
    ]
