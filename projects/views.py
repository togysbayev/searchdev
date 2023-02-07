from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .models import Project, Review
from .serializers import ProjectSerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .filters import ProjectFilter
from .permissions import IsAdminOrReadOnly, IsOwnerOfProject
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProjectFilter
    search_fields = ['title', 'description']
    ordering_fields = ['unit_price', 'last_update']
    http_method_names = ['head', 'options', 'get', 'post', 'put']
    
    # def get_permissions(self):
    #     if self.request.method == 'GET':
    #         return [AllowAny()]
    #     if self.request.method in ['DELETE', 'PUT']:
    #         return [IsOwnerOfProject()]
    #     return [IsAuthenticated()]
    
    def get_permissions(self):
        if self.request.method in ['DELETE', 'PUT']:
            return [IsOwnerOfProject()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
    
class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.filter(project=self.kwargs['project__pk'])
    
    def get_serializer_context(self):
        return {'project_id': self.kwargs['project__pk']}
    
    