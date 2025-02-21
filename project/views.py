from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .serializers import ProjectSerializer
from .models import Project
from pagination.pagination import Pagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


#listar todos los proyectos
# class ProjectList(APIView):
#     def get(self, request):
#         projects = Project.objects.all()
#         serializer = ProjectSerializer(projects, many=True)
#         return Response(serializer.data)


#listar todos los proyectos con paginacion
class ProjectList(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    #Aplicar paginación
    pagination_class = Pagination 
    permission_classes = [IsAuthenticated]



class ProjectDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Crear proyecto
class ProjectCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Editar proyecto PUT
class ProjectUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Editar proyecto PATCH
class ProjectPatch(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Eliminar proyecto
class ProjectDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

