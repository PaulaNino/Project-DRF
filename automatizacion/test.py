import sys
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_drf.settings')
django.setup()

from django.contrib.auth.models import Group, Permission

#Crear grupo 
gerente_group = Group.objects.create(name="Gerentes")

#Obtener permiso que vamos a asignar
permiso = Permission.objects.get(codename="change_user")

#Asignar el permiso a el grupo
gerente_group.permissions.add(permiso)