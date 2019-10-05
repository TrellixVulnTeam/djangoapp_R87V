# Generated by Django 2.2.5 on 2019-10-05 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anket', '0002_auto_20190914_0215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yoneticiler',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('yonetici_ad', models.CharField(max_length=250, verbose_name='')),
                ('yonetici_soyad', models.CharField(max_length=250, verbose_name='')),
                ('baglioldugu_kurum', models.CharField(max_length=250, verbose_name='')),
            ],
        ),
        migrations.AlterField(
            model_name='sorular',
            name='islem_tarihi',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
