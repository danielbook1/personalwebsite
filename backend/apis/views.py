from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from portfolio.models import Project
from .serializers import ProjectSerializer

# Create your views here.
class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class RootAPIView(APIView):
    def get(self, request):
        return Response({
            "message": "Available Endpoints",
            "endpoints": {
                "portfolio": "/api/portfolio/",
            }
        })