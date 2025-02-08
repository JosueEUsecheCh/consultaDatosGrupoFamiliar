from django.db import models
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()  # Esto carga el archivo .env
KEY = os.getenv("ENCRYPTION_KEY")  # Cargar la clave de encriptación desde el archivo .env

# Crear una instancia de Fernet con la clave
cipher_suite = Fernet(KEY)

class MyTable(models.Model):
    ci_titular = models.CharField(max_length=255, primary_key=True)
    apellidos = models.CharField(max_length=24)
    nombres = models.CharField(max_length=25)
    ci_beneficiario = models.CharField(max_length=255, blank=True, null=True)
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

    def encrypt_ci(self, ci):
        """Encripta la cédula"""
        return cipher_suite.encrypt(ci.encode()).decode()

    def decrypt_ci(self, encrypted_ci):
        """Desencripta la cédula"""
        return cipher_suite.decrypt(encrypted_ci.encode()).decode()

    def save(self, *args, **kwargs):
        # Encriptamos las cédulas antes de guardarlas
        if self.ci_titular:
            self.ci_titular = self.encrypt_ci(self.ci_titular)
        if self.ci_beneficiario:
            self.ci_beneficiario = self.encrypt_ci(self.ci_beneficiario)
        super().save(*args, **kwargs)

    def __str__(self):
        # Desencriptamos la cédula para mostrarla
        ci_titular = self.decrypt_ci(self.ci_titular) if self.ci_titular else "Desconocido"
        return f"{self.nombres} {self.apellidos} ({ci_titular})"
