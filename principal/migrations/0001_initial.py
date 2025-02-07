# Generated by Django 5.1.6 on 2025-02-06 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyTable',
            fields=[
                ('ci_titular', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('apellidos', models.CharField(max_length=24)),
                ('nombres', models.CharField(max_length=25)),
                ('ci_beneficiario', models.CharField(blank=True, max_length=20, null=True)),
                ('parentesco', models.CharField(max_length=9)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('fecha_de_nacimiento', models.DateField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('discapacidad_o_condicion_especial', models.CharField(blank=True, max_length=19, null=True)),
                ('indicar_menor_bajo_custodia_legal', models.CharField(blank=True, max_length=30, null=True)),
                ('observacion', models.CharField(blank=True, max_length=33, null=True)),
            ],
            options={
                'db_table': 'mytable',
                'managed': False,
            },
        ),
    ]
