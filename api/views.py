from django.utils import timezone
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from reference_book.models import ReferenceBook, ItemReferenceBook, ReferenceBookData
from api.serializers import ReferenceBookSerializer, ItemDetailSerializer
from rest_framework.pagination import LimitOffsetPagination

class ReferenceBookList(generics.ListAPIView):
    """Список справочников"""
    serializer_class = ReferenceBookSerializer
    queryset = ReferenceBook.objects.all()


class ItemDetailView(APIView,LimitOffsetPagination):
    """Список элементов справочника, валидация"""

    def get(self, request):
        item = ItemReferenceBook.objects.filter(reference_book__date__lte=timezone.now())

        valid_param = ['version_actual','id_book','version','limit','offset']
        for param in request.GET:
            if param not in valid_param:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                                data="Передаваемый параметр '{}' недопустим,"
                                     "запрос принимает:{}".format(param,valid_param))

        if 'version_actual' in request.GET:
            get_bool = request.GET['version_actual'].title()
            if get_bool not in ['True', 'False']:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
                                data="Значение '{}' недопустимо,"
                                     "параметр 'version_actual' ожидает получить 'True или False'".format(get_bool))
            if get_bool == 'True':
                item = item.filter(reference_book__is_active=True)
        else:
            item = item.filter(reference_book__is_active=True)

        if 'id_book' in request.GET:
            pk_book = request.GET['id_book']
            if not pk_book.isdigit():
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Значение {} недопустимо,"
                                     "параметр 'id_book' ожидает получить - целое число".format(pk_book))
            else:
                books = ReferenceBook.objects.all()
                if not books.filter(pk=pk_book).exists():
                    books_id = [x.id for x in books]
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data="Значение '{}' недопустимо,в базе присутствуют справочники с идентификаторами: {}".format(
                                        pk_book,
                                        books_id))
            item = item.filter(reference_book__reference_book__pk=pk_book)

        if 'version' in request.GET:
            version = request.GET['version']
            books_data = ReferenceBookData.objects.all()
            if pk_book:
                books_data = books_data.filter(reference_book=pk_book)
            if not books_data.filter(version=version).exists():
                version_id = [x.version for x in books_data]
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data="Значение '{}' недопустимо,в базе присутствуют версии: {}".format(version,
                                                                                                       version_id))
            item = item.filter(reference_book__version=version)

        results = self.paginate_queryset(item, request, view=self)
        serializer = ItemDetailSerializer(results, many=True)
        return self.get_paginated_response(serializer.data)


