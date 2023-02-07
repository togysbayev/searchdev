from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from .models import Profile
from .serializers import DeveloperSerializer
from .permissions import CanViewHistoryPermission, IsAdminOrReadOnly, IsOwnerOfProfile

class DeveloperViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = DeveloperSerializer
    http_method_names = ['head', 'options', 'get', 'post', 'put']
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        elif self.action == 'history':
            return [CanViewHistoryPermission()]
        elif self.action == 'me':
            return [IsAuthenticated()]
        elif self.request.method == 'PUT':
            return [IsOwnerOfProfile()]
        return [AllowAny()]
    
    def create(self, request, *args, **kwargs):
        if request.user.profile in Profile.objects.all():
            return Response({"You have already created an account!"}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)
    
    @action(detail=False, methods=['GET', 'PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        developer = Profile.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = DeveloperSerializer(developer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = DeveloperSerializer(developer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
    
    @action(detail=True, methods=['GET'], permission_classes=[CanViewHistoryPermission])
    def history(self, request, pk):
        return Response("Ok")
    