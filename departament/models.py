from django.db import models
from company.models import Company, Employee

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    company = models.ManyToManyField(Company, related_name="departments")
    employee = models.ManyToManyField(Employee, related_name="departments")
    is_active = models.BooleanField(default=True, verbose_name="Estado")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Fecha actualización")

    class Meta:
        db_table = "departments"
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name