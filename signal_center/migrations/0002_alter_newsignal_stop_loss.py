# Generated by Django 4.1.2 on 2022-10-21 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signal_center', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsignal',
            name='stop_loss',
            field=models.DecimalField(decimal_places=20, max_digits=30, verbose_name='حد ضرر'),
        ),
    ]
