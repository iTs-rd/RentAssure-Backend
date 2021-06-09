import django_filters
from django_filters.constants import EMPTY_VALUES
from .models import DataModel


class ListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value in EMPTY_VALUES:
            return qs
        value_list = value.split(",")
        qs = super().filter(qs, value_list)
        return qs

class DataFilter(django_filters.FilterSet):
    rent=django_filters.NumberFilter()
    rent__gte=django_filters.NumberFilter(field_name='rent',lookup_expr='gte')
    rent__lte=django_filters.NumberFilter(field_name='rent',lookup_expr='lte')
    
    area__lte=django_filters.NumberFilter(field_name='area',lookup_expr='lte')
    area__gte=django_filters.NumberFilter(field_name='area',lookup_expr='gte')

    # rent = ListFilter(field_name="rent", lookup_expr="in")
    property_type = ListFilter(lookup_expr="in")
    bhk = ListFilter(lookup_expr="in")
    furnishing = ListFilter(lookup_expr="in")
    available_for = ListFilter(lookup_expr="in")
    
    
    class Meta:
        model = DataModel
        fields = '__all__'

        exclude = ['img1','img2','img3','img4']
