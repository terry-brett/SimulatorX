# Generated by Django 3.2.7 on 2021-10-19 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=30)),
                ('population', models.IntegerField()),
                ('white', models.FloatField()),
                ('black', models.FloatField()),
                ('asian', models.FloatField()),
                ('other', models.FloatField()),
                ('male', models.FloatField()),
                ('female', models.FloatField()),
                ('child', models.FloatField()),
                ('adult', models.FloatField()),
                ('senior', models.FloatField()),
            ],
        ),
    ]
