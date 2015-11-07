from django.db import models
# Create your models here.

class  Usuarios(models.Model):
	Id_Usuario=models.IntegerField(primary_key=True)
	NombreUsuario=models.CharField(max_length="50", null= False, blank=False)
	Password= models.CharField(max_length="25", null= False, blank= False)
			
class TiposDeTelefonos(models.Model):
	Id_TipoTelefono= models.IntegerField(primary_key= True)
	NomreDeTipoDeTelefono=models.CharField(max_length="200", null=False, blank=False)
		

class Contactos(models.Model):
	IdContacto=models.IntegerField(primary_key=True)
	NombreContacto= models.CharField(max_length="90", null= False, blank= False)
	ApellidoMaternoContacto= models.CharField(max_length="200", null= False, blank= False)
	ApellidoPaternoContacto= models.CharField(max_length="200")
	TipoTelefono= models.ForeingKey(TiposDeTelefonos)
	CorreoElectronico= models.EmailField(max_length="150")
	Direccion= models.CharField(max_length="300", null= True, blank= True)
	PathImagen= models.CharField(max_length="700")
	Web= models.CharField(max_length="200")
	TwitterCuenta=models.CharField(max_length="30")
	FechaDeRegistro=models.DateField(null= False, blank=False)
	def __str__(self):
		return self.Id_Contacto

class NumerosTelefonos(models.Model):
	Id_NumeroTelefono= models.IntegerField(primary_key=True)
	Id_Contacto= models.ForeingKey(Contactos)
	NumeroTelefonico= models.CharField(max_length="20")

class Grupo(model.Model):
	Id_Grupo= models.IntegerField(primary_key=True)
	Id_Usuario= models.ForeingKey(Usuarios)
	NombreGrupo= models.CharField(max_length="350")
	GrupoMiembros= models.ManyToManyField(Contactos, through='Miembros')
	def __str__(self):
		return self.NombreGrupo

class  Miembros(object):
	MiembrosContacto=models.ForeingKey(Contactos)
	MiembrosGrupo= models.ForeingKey(Grupo)

