# Generated by Django 2.1.2 on 2018-11-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20181105_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='db.Item'),
        ),
    ]