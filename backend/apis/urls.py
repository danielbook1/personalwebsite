from django.urls import path
from .views import ProjectListView, RootAPIView, ProjectDetail

urlpatterns = [
    path("portfolio/", ProjectListView.as_view(), name="project_list"),
    path("portfolio/<int:pk>/", ProjectDetail.as_view(), name="project_detail"),
    path("", RootAPIView.as_view(), name="endpoint_list"),
]