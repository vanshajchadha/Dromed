# Generated by Django 2.1.2 on 2018-11-07 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_item_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='qty_avail',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]