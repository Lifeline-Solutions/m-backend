# Generated by Django 4.2.3 on 2023-08-21 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_match_time_alter_match_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='stadium',
            field=models.CharField(blank=True, default='St Sebastian Park', max_length=200, null=True),
        ),
    ]