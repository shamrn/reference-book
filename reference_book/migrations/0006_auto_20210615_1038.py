# Generated by Django 3.2.4 on 2021-06-15 07:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0005_auto_20210615_0915'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referencebookdata',
            old_name='ident',
            new_name='reference_book',
        ),
        migrations.AlterUniqueTogether(
            name='referencebookdata',
            unique_together=set(),
        ),
    ]
