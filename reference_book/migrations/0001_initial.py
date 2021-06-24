# Generated by Django 3.2.4 on 2021-06-14 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReferenceBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Наименование справочника')),
                ('short_name', models.CharField(max_length=50, verbose_name='Короткое наименование')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('version', models.CharField(max_length=200, unique=True, verbose_name='Версия')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Начало действия справочника')),
            ],
            options={
                'verbose_name': 'Справочник',
                'verbose_name_plural': 'Справочник',
            },
        ),
        migrations.CreateModel(
            name='ItemReferenceBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, verbose_name='Код')),
                ('value', models.CharField(max_length=50, verbose_name='Значение элемента')),
                ('desc_value', models.TextField(verbose_name='Описание элемента')),
                ('reference_book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reference_book.referencebook', verbose_name='Справочник')),
            ],
            options={
                'verbose_name': 'Элемент справочника',
                'verbose_name_plural': 'Элемент справочника',
            },
        ),
    ]
