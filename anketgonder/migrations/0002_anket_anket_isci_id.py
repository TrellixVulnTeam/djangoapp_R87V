# Generated by Django 2.2.7 on 2019-11-14 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anket', '__first__'),
        ('anketgonder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anket',
            name='anket_isci_id',
            field=models.ManyToManyField(to='anket.Isciler'),
        ),
    ]
