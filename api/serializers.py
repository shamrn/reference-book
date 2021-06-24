from django.utils import timezone
from rest_framework import serializers
from reference_book.models import ReferenceBook, ReferenceBookData, ItemReferenceBook
from datetime import datetime




class FilteredListSerializer(serializers.ListSerializer):
    """Фильтрация версий"""

    def to_representation(self, data):
        data = data.filter(date__lte=timezone.now())
        get_params = self.context['request'].query_params
        if 'is_active' in get_params:
            is_active = get_params['is_active'].title()
            if is_active not in ['True', 'False']:
                raise serializers.ValidationError("Значение '{}' в поле 'is_active' недопустимо,"
                                    "параметр 'is_active' ожидает получить 'True или False'".format(is_active))
            elif is_active == 'False':
                data = data.filter()
        else:
            data = data.filter(is_active=True)
        if 'date' in get_params:
            date = get_params['date']
            try:
                datetime.strptime(date, "%Y-%m-%d")
                data = data.filter(date__lte=date)
            except ValueError:
                raise serializers.ValidationError("Недопустимый формат даты, ожидается получить '2021-05-25'")

        return super(FilteredListSerializer, self).to_representation(data)


class ReferenceBookDataSerializer(serializers.ModelSerializer):
    """Сериализация данных и версий справочника"""
    count_item = serializers.IntegerField(source='get_count_item')
    class Meta:
        list_serializer_class = FilteredListSerializer
        model = ReferenceBookData
        fields = ('id', 'name','short_name','desc','version','date','count_item','is_active')


class ReferenceBookSerializer(serializers.ModelSerializer):
    """Сериализация справочника"""
    version = ReferenceBookDataSerializer(many=True)
    class Meta:
        model = ReferenceBook
        fields = ('id','version')

class ItemReferenceBookSerializer(serializers.ModelSerializer):
    """Сериализация id и name справочника"""
    class Meta:
        model = ReferenceBookData
        fields = ('id','short_name')

class ItemDetailSerializer(serializers.ModelSerializer):
    """Серилизация элементов справочника"""
    reference_book = ItemReferenceBookSerializer()

    class Meta:
        model = ItemReferenceBook
        fields = '__all__'

