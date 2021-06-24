from django.forms.utils import ErrorList
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, ListView
from .models import ReferenceBook, ReferenceBookData, ItemReferenceBook
from .forms import UpdateBookForm
from .version import edit_version


def index(request):
    """Главная страница"""
    ref_books = ReferenceBook.objects.all()
    context = {'ref_books': ref_books}
    return render(request, 'reference_book/index.html', context=context)


class CreateBookView(CreateView):
    """Создание справочника"""
    model = ReferenceBookData
    fields = ('name', 'short_name', 'desc', 'version', 'date')
    template_name = 'reference_book/create_book.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        reference_book = ReferenceBook.objects.create()
        instance = form.save(commit=False)
        instance.reference_book = reference_book
        instance.save()
        return super(CreateBookView, self).form_valid(form)


def version_book(request, pk, pk_version=None):
    """Список версий справочника
    Изменение активной версии справочника
    pk - индификатор справочника
    pk_version - индификатор версии"""

    if pk_version:
        vers_book = ReferenceBookData.objects.get(pk=pk_version)
        vers_book.is_active = True
        edit_version(pk)
        vers_book.save()
    ref_books = ReferenceBookData.objects.filter(reference_book__pk=pk)  # все версии словаря
    context = {'ref_books': ref_books, 'book_pk': pk}
    return render(request, 'reference_book/version_book.html', context=context)


class UpdateBookView(UpdateView):
    """Редактирование версий справочника"""
    model = ReferenceBookData
    form_class = UpdateBookForm
    template_name = 'reference_book/update_book.html'
    success_url = reverse_lazy('index')


class NewVersionBookView(CreateView):
    """Создание новой версии справочника"""
    model = ReferenceBookData
    fields = ('name', 'short_name', 'desc', 'version', 'date', 'is_active')
    template_name = 'reference_book/create_book.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        book_pk = self.kwargs['pk']
        reference_book = ReferenceBook.objects.get(pk=book_pk)
        instance = form.save(commit=False)
        instance.reference_book = reference_book
        if instance.is_active:  # если пользователь захочет сделать новую версию - активной
            edit_version(book_pk)
        try:
            instance.save()
        except:
            form._errors["version"] = ErrorList([u"Такая версия уже есть, в данном справочнике"])
            return super(NewVersionBookView, self).form_invalid(form)
        return super(NewVersionBookView, self).form_valid(form)


class ListItemView(ListView):
    """Список элементов справочника"""
    model = ItemReferenceBook
    context_object_name = 'items'
    template_name = 'reference_book/list_item.html'

    def get_queryset(self):
        book_pk = self.kwargs['pk']
        items = ItemReferenceBook.objects.filter(reference_book__reference_book__id=book_pk)
        return items

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_pk'] = ReferenceBook.objects.get(pk=self.kwargs['pk']).pk
        return context


class CreateItemView(CreateView):
    """Добавление элементов в справочник"""

    model = ItemReferenceBook
    fields = ('reference_book', 'code', 'value')
    template_name = 'reference_book/create_item.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        """Фильтруем версии, выводим версии текущего справочника"""
        context = super(CreateItemView, self).get_context_data(**kwargs)
        reference_book = ReferenceBookData.objects.filter(reference_book__pk=self.kwargs['book_pk'])
        context['form'].fields['reference_book'].queryset = reference_book
        return context


class UpdateItemView(CreateItemView, UpdateView):
    """Редактирование элементов"""
