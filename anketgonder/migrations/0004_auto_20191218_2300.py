# Generated by Django 2.2.7 on 2019-12-18 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anketgonder', '0003_auto_20191218_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anket',
            name='mail_mesaj',
            field=models.TextField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='anket',
            name='subject',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
