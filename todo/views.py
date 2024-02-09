from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Todo
from .serializer import TdoSerializer



class TodoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Todo.objects.all().order_by('-date_joined')
    serializer_class = TdoSerializer
    permission_classes = [] #permissions.IsAuthenticated

