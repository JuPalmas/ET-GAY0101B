# Generated by Django 3.1.2 on 2021-06-23 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_post_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='autor',
        ),
        migrations.AddField(
            model_name='post',
            name='precio',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
