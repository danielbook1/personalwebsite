from django.urls import path
from .views import ProjectList, RootAPIView, ProjectDetail, MessageCreate

urlpatterns = [
    path("", RootAPIView.as_view(), name="endpoint_list"),
    path("portfolio/", ProjectList.as_view(), name="project_list"),
    path("portfolio/<int:pk>/", ProjectDetail.as_view(), name="project_detail"),
    path("contact/", MessageCreate.as_view(), name="create_message")
]