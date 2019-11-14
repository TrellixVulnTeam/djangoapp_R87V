# Generated by Django 2.2.7 on 2019-11-14 19:19

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anket', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anket',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('anket_adi', models.CharField(max_length=100)),
                ('islem_tarihi', models.DateTimeField()),
                ('kullanici_adi', models.CharField(default=django.contrib.auth.models.User, max_length=50)),
                ('anket_soru_id', models.ManyToManyField(to='anket.Sorular')),
            ],
        ),
    ]
