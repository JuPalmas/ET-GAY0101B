# Generated by Django 3.1.2 on 2021-06-23 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_post_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comuna',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='direccion',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
