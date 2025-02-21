from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .serializers import DepartmentSerializer
from .models import Department
from pagination.pagination import Pagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


#listar todos los departamentos
# class DepartmentList(APIView):
#     def get(self, request):
#         projects = Department.objects.all()
#         serializer = DepartmentSerializer(projects, many=True)
#         return Response(serializer.data)


#listar todos los departamentos con paginacion
class DepartmentList(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    #Aplicar paginación
    pagination_class = Pagination 
    permission_classes = [IsAuthenticated]



class DepartmentDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        project = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Crear proyecto
class DepartmentCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Editar proyecto PUT
class DepartmentUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        project = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Editar proyecto PATCH
class DepartmentPatch(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        project = get_object_or_404(Department, pk=pk)
        serializer = DepartmentSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Eliminar proyecto
class DepartmentDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        project = get_object_or_404(Department, pk=pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

