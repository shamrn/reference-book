# Generated by Django 3.2.4 on 2021-06-16 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0007_auto_20210615_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencebookdata',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Сделать эту версию активной'),
        ),
    ]
