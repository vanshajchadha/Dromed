# Generated by Django 2.1.2 on 2018-11-13 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0016_auto_20181113_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_asoc_order',
            name='itemNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='item_asoc_order',
            name='orderNo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='item_asoc_order',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
