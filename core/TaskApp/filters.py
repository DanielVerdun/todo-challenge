import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):

    created_at = django_filters.DateFromToRangeFilter(field_name='created_at')
    description__icontains = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['created_at', 'description__icontains']