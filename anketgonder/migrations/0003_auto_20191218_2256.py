# Generated by Django 2.2.7 on 2019-12-18 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anketgonder', '0002_anket_anket_isci_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='anket',
            name='mail_mesaj',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='anket',
            name='subject',
            field=models.TextField(max_length=100, null=True),
        ),
    ]
