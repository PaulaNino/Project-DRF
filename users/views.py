from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import Group, Permission
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, UserLoginSerializer
from .models import User
from pagination.pagination import Pagination
from rest_framework.generics import ListAPIView
from rest_framework.permissions import DjangoModelPermissions


#-------------LOGIN----------------
#Inicio de sesión
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_email= serializer.validated_data['email']
        user = User.objects.get(email=user_email)

        refresh = RefreshToken.for_user(user)

        response_data = {
            'user_id': user.id,
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone': user.phone,
            'password': user.password,
            'is_active': user.is_active,
            'refresh': str(refresh),
            'access': str(refresh.access_token),

        }
       

        return Response(response_data, status=status.HTTP_200_OK)

# def generate_login_response(user, request):
#     """
#     Método auxiliar para generar la respuesta de inicio de sesión.
#     """
#     refresh = RefreshToken.for_user(user)
    
#     return {
#         'refresh': str(refresh),
#         'access': str(refresh.access_token),
#         'user_id': user.id,
#         'email': user.email,
#         "first_name": user.first_name,
#         "last_name": user.last_name,
#     }

# class UserLoginView1(APIView):
#     """
#     Vista para iniciar sesión.
#     """
#     def post(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.is_valid(raise_exception=True)
#             user = serializer.validated_data['email']
#             response_data = generate_login_response(user, request)
#             return Response(response_data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#-------------ROL----------------
#Crear rol
class RoleCreate(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Crea un nuevo rol con nombre y id de los permisos 
        """
        role_name = request.data.get("name")
        permissions_ids = request.data.get("permissions", []) 


        #Valida que se ingrese el nombre
        if not role_name:
            return Response({"error": "El nombre del rol es obligatorio."}, status=status.HTTP_400_BAD_REQUEST)

        # Crear el grupo si no existe
        role, created = Group.objects.get_or_create(name=role_name)

        # Obtener los permisos por ID
        permissions = Permission.objects.filter(id__in=permissions_ids)

        #Valida que los id de los permisos ingresados existan en la base de datos
        if len(permissions) != len(permissions_ids):
            return Response({"error": "Uno o más permisos no existen."}, status=status.HTTP_400_BAD_REQUEST)

        # Asignar los permisos al grupo
        role.permissions.set(permissions)

        return Response({"message": "Rol creado exitosamente.", "role": role_name}, status=status.HTTP_201_CREATED)


#-------------USUARIOS----------------
#listar todos los usuarios
# class UserList(APIView):
#     permission_classes = [IsAuthenticated]
#     def get(self, request):
#         users = User.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
    
#listar todos los usuarios con paginacion
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #Aplicar paginación
    pagination_class = Pagination 
    permission_classes = [IsAuthenticated]

    
class UserDetail(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

#Crear usuario
class UserCreate(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Editar usuario PUT
class UserUpdate(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Editar usuario PATCH
class UserPatch(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#Eliminar usuario
class UserDelete(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
