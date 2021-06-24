from django.core.exceptions import ValidationError
from django.db import models


class ReferenceBook(models.Model):
    """Модель индификатора справочника"""
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')

    def __str__(self):
        return f'Уникальный идентификатор справочника {self.id}'

    class Meta:
        verbose_name = 'Cправочник'
        verbose_name_plural = 'Cправочники'

class ReferenceBookData(models.Model):
    """Модель данных справочника"""
    reference_book = models.ForeignKey(ReferenceBook, on_delete=models.CASCADE,
                                       verbose_name='Идентификатор cправочника',
                                       related_name='version')
    name = models.CharField('Наименование справочника', max_length=200)
    short_name = models.CharField('Короткое наименование', max_length=50)
    desc = models.TextField('Описание')
    version = models.CharField('Версия', max_length=200, unique=False)
    date = models.DateField('Начало действия справочника', help_text="Пример даты - 15.06.2102")
    is_active = models.BooleanField(default=True, verbose_name='Сделать эту версию активной')

    class Meta:
        unique_together = ['reference_book', 'version']
        verbose_name = 'Версия справочника'
        verbose_name_plural = 'Версии справочника'

    def __str__(self):
        return self.version

    @property
    def get_count_item(self):
        return self.item.count()


class ItemReferenceBook(models.Model):
    """Модель элемента справочника"""
    reference_book = models.ForeignKey(ReferenceBookData,
                                       related_name='item',
                                       on_delete=models.CASCADE,
                                       verbose_name='Версия справочника')
    code = models.CharField('Код', max_length=200)
    value = models.CharField('Значение элемента', max_length=50)

    class Meta:
        unique_together = ['reference_book', 'code']
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элемент справочника'

    def __str__(self):
        return 'код - {} значение - {}'.format(self.code, self.value)

