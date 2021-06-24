from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.html import format_html

from .models import ReferenceBook,ReferenceBookData, ItemReferenceBook
import nested_admin

class ItemReferenceBookAdmin(nested_admin.NestedStackedInline):
    model = ItemReferenceBook
    extra = 1

class ReferenceBookDataAdmin(nested_admin.NestedStackedInline):
    model = ReferenceBookData
    inlines = [ItemReferenceBookAdmin]
    extra = 1

@admin.register(ReferenceBook)
class ReferenceBookAdmin(nested_admin.NestedModelAdmin):
    model = ReferenceBook
    inlines = [ReferenceBookDataAdmin]

    def change_button(self, obj):
        return format_html('<a href="/admin/reference_book/referencebook/{}/change/">Редактировать</a>', obj.id)

    def count_version_button(self, obj):
        return format_html('<p>Кол-во версий: {}</p>', obj.version.count())

    def name_book(self,obj):
        name_book = ReferenceBookData.objects.filter(reference_book__pk=obj.pk).last().short_name
        return format_html('<p>{}</p>', name_book)

    change_button.short_description = "Редактирование"
    count_version_button.short_description = 'Кол-во версий'
    name_book.short_description = 'Название справочника последней версии'
    list_display = ('change_button','name_book','count_version_button')



admin.site.unregister([User, Group])