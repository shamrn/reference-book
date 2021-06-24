from .models import ReferenceBookData


def edit_version(book_pk):
    """Функция, меняет статусы версий - на неактивный"""
    reference_book = ReferenceBookData.objects.filter(reference_book__pk=book_pk)

    for book in reference_book:
        book.is_active = False
        book.save()
