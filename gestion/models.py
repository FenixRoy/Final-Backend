from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class equipo(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    tipo = models.TextField(null=False, max_length=100)
    marca = models.TextField(null=False, max_length=100)
    modelo = models.TextField(null=False, max_length=100)
    numero_serie = models.CharField(null=False, unique=True, max_length=100)
    class Meta:
        db_table = "equipos"
        ordering = ["tipo", "modelo"]
        unique_together = ["numero_serie"]


class colaborador(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.TextField(null=False, max_length=100)
    apellido = models.TextField(null=False, max_length=100)
    dni = models.IntegerField(null=False, unique=True, validators=[
            MinValueValidator(00000000),
            MaxValueValidator(99999999)
        ])
    email = models.EmailField(null=False, unique=True, max_length=200)
    departamento = models.TextField(null=False, max_length=100)
    puesto = models.TextField(null=False, max_length=100)
    class Meta:
        db_table = "colaboradores"
        ordering = ["nombre", "apellido"]
        unique_together = ["dni"]

class tecnico(models.Model):
    id = models.AutoField(primary_key=True, unique=True, null=False)
    nombre = models.TextField(null=False, max_length=100)
    apellido = models.TextField(null=False, max_length=100)
    usuario = models.CharField(null=False, unique=True, max_length=100)
    password = models.TextField(null=False, max_length=100)
    class Meta:
        db_table = "tecnicos"
        ordering = ["nombre", "apellido"]
        unique_together = ["usuario"]

class asignacion(models.Model):
    opciones_estado = {
        ("asignado", "Asignado"),
        ("disponible", "Disponible") 
    }

    id = models.AutoField(primary_key=True, unique=True, null=False)
    equipo = models.ForeignKey(equipo, on_delete=models.PROTECT, db_column="id_equipo", unique=True)
    colaborador = models.ForeignKey(colaborador, on_delete=models.PROTECT, db_column="id_colaborador")
    tecnico = models.ForeignKey(tecnico, on_delete=models.PROTECT, db_column="id_tecnico")
    fecha_asignacion = models.DateTimeField(null=False)
    estado = models.TextField(null=False, choices=opciones_estado)
    class Meta:
        db_table = "asignaciones"
        ordering = ["fecha_asignacion"]

