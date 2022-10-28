from email.policy import default
from pyexpat import model
from tabnanny import verbose
from django.db import models
from django.forms import model_to_dict

# Create your models here.

class Vacante(models.Model):

    TIPOS_DE_VACANTE = (
    ("De Trabajo", "De Trabajo"),
    ("Servicio Social", "Servicio Social"),
    ("Prácticas Profesionales", "Prácticas Profesionales"))

    nombre=models.CharField(null=False, blank=False, max_length=50, db_column='nombre')
    empresa=models.CharField(null=False, blank=False, max_length=70, db_column='empresa')
    tipo_vacante=models.CharField(max_length=30, blank=False, null=False, choices=TIPOS_DE_VACANTE, default="SS", db_column='tipo_de_vacante')
    carrera=models.CharField(max_length=5, null=False, blank=False, db_column="carrera")
    grado_minimo=models.CharField(max_length=20, null=False, blank=False, db_column="grado_minimo")
    descripcion=models.TextField(null=False, blank=False, db_column='descripcion')
    responsabilidades=models.TextField(null=False, blank=False, db_column='responsabilidades')
    requerimientos=models.TextField(null=False, blank=False, db_column='requerimientos')
    contacto=models.CharField(max_length=70, null=False, blank=False, db_column="contacto", default='Sin Contacto')

    class Meta:
        db_table='VacanteServicio'
        default_permissions=()
        verbose_name='Vacante de Servicio'
        verbose_name_plural='Vacantes de Servicio'
