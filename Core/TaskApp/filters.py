import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):

    """
    created_at__gte: Fecha de creación mayor o igual a una fecha dada.
    created_at__lte: Fecha de creación menor o igual a una fecha dada.
    content__icontains: Contenido que contiene una cadena dada (ignorando mayúsculas/minúsculas).

    """
    created_at__gte = django_filters.DateFilter(field_name='created_at', lookup_expr='gte')
    created_at__lte = django_filters.DateFilter(field_name='created_at', lookup_expr='lte')
    content__icontains = django_filters.CharFilter(field_name='description', lookup_expr='icontains')

    class Meta:
        model = Task
        fields = ['created_at__gte', 'created_at__lte', 'content__icontains']