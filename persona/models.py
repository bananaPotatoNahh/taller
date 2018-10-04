from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre=models.CharField(max_length=100)
    apellidoPaterno=models.CharField(max_length=100)
    apellidoMaterno=models.TextField
    edad=models.IntegerField
    sexo=models.TextField
    fechaNacimiento=models.DateField
    ocupacion=models.TextField
    direccion=models.TextField
    telefono=models.IntegerField
    gradoDeInstruccion=models.CharField
    estadoCivil=models.CharField
    nacionesOriginarias=models.TextField
    IdiomaODialecto=models.CharField


class AntecedentesPatologicos(models.Model):
    anemia=models.CharField
    asma=models.CharField
    cardiopatias=models.CharField
    enfGastricas=models.CharField
    hepatitis=models.CharField
    tuberculosis=models.CharField
    diabetesMel=models.CharField
    epilepsia=models.CharField
    hipertension=models.CharField
    vih=models.CharField
    otros=models.CharField
    alergias=models.CharField
    embarazo=models.CharField
    semanas=models.IntegerField
    tratamientoMedico=models.CharField
    recibeMedicacion=models.CharField
    hemorragiaExtracionDental=models.CharField
    inmediataMediana=models.CharField
    pertenece = models.ForeignKey(Persona, related_name='antecedentespatologiocs', on_delete=models.DO_NOTHING)

class examenes(models.Model):
    labios=models.CharField
    lengua=models.CharField
    paladar=models.CharField
    pisoDeLaBoca=models.CharField
    mucosaYugal=models.CharField
    encias=models.CharField
    protesisDental=models.CharField
    atm=models.CharField
    gangliosLinfatico=models.CharField
    respiradorNasal=models.CharField
    respiradorBucal=models.CharField
    respiradorBuconasal=models.CharField
    Otros=models.CharField
    pertenece = models.ForeignKey(Persona, related_name='examenes', on_delete=models.DO_NOTHING)


class antecedentes(models.Model):
    fechaUltimaVisitaOdontologo=models.DateField
    fuma=models.CharField
    bebe=models.CharField
    otro=models.CharField
    utilzaCepillo=models.CharField
    utilizaHilo=models.CharField
    utilizaEnjuagueBucal=models.CharField
    frecuenciaCepillo=models.CharField
    enciasSangran=models.CharField
    higieneBucal=models.CharField
    pertenece = models.ForeignKey(Persona, related_name='antecedentes', on_delete=models.DO_NOTHING)
