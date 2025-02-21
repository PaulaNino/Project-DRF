from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from .serializers import CompanySerializer, EmployeeSerializer
from .models import Company, Employee
from pagination.pagination import Pagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


#listar todas las empresas
# class CompanyList(APIView):
#     def get(self, request):
#         Companies = Company.objects.all()
#         serializer = CompanySerializer(Companies, many=True)
#         return Response(serializer.data)


#listar todos los empresas con paginacion
class CompanyList(ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    #Aplicar paginación
    pagination_class = Pagination 
    permission_classes = [IsAuthenticated]



class CompanyDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Crear empresa
class CompanyCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Editar empresa PUT
class CompanyUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Editar empresa PATCH
class CompanyPatch(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        serializer = CompanySerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Eliminar empresa
class CompanyDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        company = get_object_or_404(Company, pk=pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



#---------------------Empleados ------------------------

       
#listar todos los empleados
# class EmployeeList(APIView):
#     def get(self, request):
#         employees = Employee.objects.all()
#         serializer = EmployeeSerializer(employees, many=True)
#         return Response(serializer.data)


#listar todos los empleados con paginacion
class EmployeeList(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    #Aplicar paginación
    pagination_class = Pagination 
    permission_classes = [IsAuthenticated]





class EmployeeDetail(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Crear empleados
class EmployeeCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Editar empleados PUT
class EmployeeUpdate(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Editar empleados PATCH
class EmployeePatch(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Eliminar empleados
class EmployeeDelete(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)