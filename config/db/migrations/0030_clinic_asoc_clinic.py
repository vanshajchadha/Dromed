# Generated by Django 2.1.2 on 2018-11-19 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0029_auto_20181119_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinic_Asoc_Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinicID1', models.IntegerField()),
                ('clinicID2', models.IntegerField()),
                ('distance', models.FloatField()),
            ],
        ),
    ]
