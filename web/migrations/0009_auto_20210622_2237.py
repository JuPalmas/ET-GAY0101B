# Generated by Django 3.1.2 on 2021-06-23 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_delete_publicacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Disponible'), ('b', 'Agotado'), ('c', 'Pausada'), ('d', 'No disponible')], default='a', help_text='Disponibilidad', max_length=1),
        ),
    ]
