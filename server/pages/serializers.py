from rest_framework import serializers
from pages.models import ProjectInfo
class ProjectInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProjectInfo
        fields = ['name','description','github','demo','image']
