# Generated by Django 3.1.2 on 2021-06-23 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20210622_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='published_date',
            new_name='fecha_publicacion',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='titulo',
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Disponible'), ('b', 'Agotado'), ('c', 'Pausada'), ('d', 'No disponible')], default='d', help_text='Disponibilidad', max_length=1),
        ),
    ]