from django.db import models

class MyTable(models.Model):
    ci_titular = models.CharField(max_length=20, primary_key=True)
    apellidos = models.CharField(max_length=24)
    nombres = models.CharField(max_length=25)
    ci_beneficiario = models.CharField(max_length=20, blank=True, null=True)
    parentesco = models.CharField(max_length=9)
    sexo = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')])
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    discapacidad_o_condicion_especial = models.CharField(max_length=19, blank=True, null=True)
    indicar_menor_bajo_custodia_legal = models.CharField(max_length=30, blank=True, null=True)
    observacion = models.CharField(max_length=33, blank=True, null=True)

    class Meta:
        managed = False  # Django no gestionará esta tabla
        db_table = 'mytable'

    def __str__(self):
        return f"{self.nombres} {self.apellidos} ({self.ci_titular})"
