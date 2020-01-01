# Generated by Django 2.2.7 on 2019-12-26 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anket', '__first__'),
        ('anketgonder', '0005_auto_20191220_1146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cevaplar',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('islem_tarihi', models.DateTimeField(auto_now_add=True)),
                ('anket_isci_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anket.Isciler')),
                ('anket_soru_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anket.Sorular')),
            ],
        ),
    ]
