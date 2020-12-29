from django.shortcuts import render
from pages.models import ProjectInfo
from rest_framework import generics
from pages.serializers import ProjectInfoSerializer

# Project Info viewset
# allows us to create a CRUD api without specifying methods for functionality

class ProjectInfoList(generics.ListCreateAPIView):

    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializer