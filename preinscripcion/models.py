from django.db import models
#from django.db.models.fields import CharField

# Create your models here.
class Tutor(models.Model):
    id_tutor=models.AutoField(primary_key=True)
    nombre_t=models.CharField(max_length=50)
    ap_paterno_t=models.CharField(max_length=50)
    ap_materno_t=models.CharField(max_length=50)
    calle_t=models.CharField(max_length=50)
    numero_casa_t=models.CharField(max_length=50)
    colonia_t=models.CharField(max_length=50)
    ciudad_t=models.CharField(max_length=50)
    estado_t=models.CharField(max_length=50)
    telefono_t=models.CharField(max_length=50)
    ocupacion=models.CharField(max_length=50)
    escolaridad=models.CharField(max_length=50)
    l_parentescos=(('Madre','Madre'),('Padre','Padre'),('Tia','Tia'),('Tio','Tio'),('Abuela','Abuela'),('Abuelo','Abuelo'),('Hermana','Hermana'),('Hermano','Hermano'))
    parentesco=models.CharField(max_length=10,choices=l_parentescos)
    edad_t=models.CharField(max_length=3)
    fecha_nacimiento_t=models.DateField()
    email_t=models.CharField(max_length=50)
    nacionalidad_t=models.CharField(max_length=50)

    def nombreCompletoTutor(self):
        cadena="{2} {3}, {1}"
        return cadena.format(self.ap_paterno_t, self.ap_materno_t,self.nombre_t)

    def _str_(self):
        return self.nombreCompleto()

class EscuelaPrimaria(models.Model):
    id_primaria=models.AutoField(primary_key=True)
    nombre_e=models.CharField(max_length=50,null=False)
    clave_ct=models.CharField(max_length=12,null=False)
    calle_e=models.CharField(max_length=50)
    colonia_e=models.CharField(max_length=50)
    municipio_e=models.CharField(max_length=50)
    estado_e=models.CharField(max_length=50)

    def _str_(self):
        return "{(2)} {1}".format(self.clave_ct,self.nombre_e)

class Alumno(models.Model):
    id_alumno=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50)
    ap_paterno=models.CharField(max_length=50)
    ap_materno=models.CharField(max_length=50)
    calle=models.CharField(max_length=50) 
    num_casa_a=models.CharField(max_length=10)
    colonia_a=models.CharField(max_length=50)
    ciudad_a=models.CharField(max_length=50)
    estado_a=models.CharField(max_length=50)
    pais_a=models.CharField(max_length=50)
    fecha_nacimiento=models.DateField()
    sexos=(('M','Mujer'),('H','Hombre'))
    sexo=models.CharField(max_length=1,choices=sexos)
    telefono_alumno=models.CharField(max_length=10)
    matricula=models.CharField(max_length=8)
    curp_a=models.CharField(max_length=18)
    email_alumno=models.CharField(max_length=80)
    promedio_quinto_grado=models.FloatField(max_length=3)#revisar el lenght y el incremnto
    id_tutor=models.ForeignKey(Tutor,null=False,blank=False,on_delete=models.CASCADE)
    id_primaria=models.ForeignKey(EscuelaPrimaria,null=False,blank=False,on_delete=models.CASCADE)

    def nombreCompleto(self):
        cadena="{2} {3}, {1}"
        return cadena.format(self.ap_paterno, self.ap_materno,self.nombre)

    def _str_(self):
        return self.nombreCompleto()



