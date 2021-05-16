import django_filters
from .models import DataModel

class DataFilter(django_filters.FilterSet):
    class Meta:
        model = DataModel
        fields = '__all__'
        exclude = ['img1','img2','img3','img4']