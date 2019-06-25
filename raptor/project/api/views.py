from rest_framework import generics
from project.models import Project, Build, Results
from .serializers import ProjectSerializer, BuildSerializer, ResultSerializer


class ProjectView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrive
    """
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()

    # def get_object(self):
    #     pk = self.kwargs.get("pk")
    #     return Project.objects.get(pk=pk)


class BuildView(generics.RetrieveUpdateDestroyAPIView):
    """
    Update
    """
    serializer_class = BuildSerializer

    def get_queryset(self):
        return Build.objects.all()


class ResultsView(generics.RetrieveUpdateDestroyAPIView):
    """
    Update
    """
    serializer_class = ResultSerializer

    def get_queryset(self):
        return Results.objects.all()
