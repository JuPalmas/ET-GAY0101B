# Generated by Django 3.2.4 on 2021-06-28 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20210623_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='autor',
            field=models.CharField(max_length=200),
        ),
    ]
