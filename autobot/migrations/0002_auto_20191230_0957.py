# Generated by Django 3.0.1 on 2019-12-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autobot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
