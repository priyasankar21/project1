# Generated by Django 3.1.6 on 2021-05-14 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vinayaga', '0010_auto_20210514_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='Email',
            field=models.EmailField(max_length=20),
        ),
    ]
