from datetime import timezone
from django.db import models
from datetime import date
from company.models import Employee

class Project(models.Model):
    STATUS_CHOICES = [
        ("not_started", "Sin iniciar"),
        ("in_progress", "En proceso"),
        ("completed", "Terminado"),
        ("canceled", "Cancelado"),
    ]
    name = models.CharField(max_length=255, unique=True, verbose_name="Project Name")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    employee = models.ManyToManyField(Employee,  related_name="projects")
    start_date = models.DateField(default=date.today, verbose_name="Start Date")
    end_date = models.DateField(blank=True, null=True, verbose_name="End Date")
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True, verbose_name="Budget")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="not_started", verbose_name="Status")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

   

    def __str__(self):
        return self.name