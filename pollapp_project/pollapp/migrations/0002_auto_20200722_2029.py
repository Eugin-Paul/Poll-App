# Generated by Django 3.0.8 on 2020-07-22 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='option_four',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='poll',
            name='option_four_count',
            field=models.IntegerField(default=0),
        ),
    ]
