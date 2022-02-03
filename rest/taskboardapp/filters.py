from django_filters import rest_framework as filters
from rest.taskboardapp.models import WorkProject


class WorkProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = WorkProject
        fields = ['name']
