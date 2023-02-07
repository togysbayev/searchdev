from django_filters.rest_framework import FilterSet
from .models import Project

class ProjectFilter(FilterSet):
  class Meta:
    model = Project
    fields = {
      'title': ['exact', 'contains'],
      'owner': ['exact'],
      'vote_ratio': ['gt', 'lt']
    }
