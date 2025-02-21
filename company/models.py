from django.db import models
from django.utils import timezone

#Modelo de empresa
class Company(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, verbose_name="Nombre")
    nit = models.CharField(max_length=20, unique=True, verbose_name="NIT")
    address = models.CharField(max_length=300, verbose_name="Dirección")
    phone = models.CharField(max_length=20, verbose_name="Telefono")
    industry = models.CharField(max_length=100, blank=True, null=True, verbose_name="Sector")  
    created_at = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    
    def __str__(self):
        return self.name
    


#Modelo de empleado
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=False, null=False,related_name='employees')
    first_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Apellido')
    position = models.CharField(max_length=100, blank=False, null=False, verbose_name='Cargo')
    hire_date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")


    def __str__(self):
        return f"{self.first_name} {self.last_name}"
