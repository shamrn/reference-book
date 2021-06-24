# Generated by Django 3.2.4 on 2021-06-17 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reference_book', '0009_alter_itemreferencebook_reference_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencebookdata',
            name='reference_book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='version', to='reference_book.referencebook', verbose_name='Идентификатор cправочника'),
        ),
        migrations.AlterUniqueTogether(
            name='referencebookdata',
            unique_together={('reference_book', 'version')},
        ),
    ]