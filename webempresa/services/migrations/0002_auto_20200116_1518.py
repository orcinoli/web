# Generated by Django 3.0.2 on 2020-01-16 18:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['-created'], 'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
        migrations.RenameField(
            model_name='service',
            old_name='create',
            new_name='created',
        ),
    ]
