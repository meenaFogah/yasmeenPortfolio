from django.urls import path
from pages.views import ProjectInfoList

urlpatterns = [
    path('',ProjectInfoList.as_view()),
]