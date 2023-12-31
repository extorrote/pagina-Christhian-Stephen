from django.db import models

# Create your models here.

#PARA INDICAR QUE ESTO ES UN MODELO Y NO UNA CLASE NORMAL LE PASO EL (models.Model)
class Tus_Pedidos (models.Model):
    Title=models.CharField(max_length=250, verbose_name="Titulo")
    Content=models.TextField(max_length=400, verbose_name="Contenido")#ESTO ES UN CAMPO DE TEXTO MUY GRANDE
    image=models.ImageField(default='null',verbose_name="imagen del Poducto")
    Street=models.CharField(max_length=100, verbose_name="Calle")
    House_number=models.SmallIntegerField(verbose_name="Numero de Casa")# AQUI LE HABIA PUESTO max_length=10 PERO AL HACER LA MIGRACION ME SALIO QUE LO IGNORO PORQUE NO DEBO PONERLE ESO A UN SMALLfield
    House_Description=models.CharField(max_length=500, verbose_name="Describe tu Casa")
    public=models.BooleanField(verbose_name="Publico")
    Created_at=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    Updated_at=models.DateTimeField(auto_now=True, verbose_name="Fecha de Modificacion")
    class Meta:
        verbose_name="Tu Pedido"
        verbose_name_plural="Tus Pedidos"
        ordering=['id']#SI LE PONGO EL - ORDENA INVERSAMENTE puedo ordenar por public o por lo que le quiera poner COMO created_at Y IGUAL SI LE PONGO EL - ORDENA DEL MAS VIEJO AL MAS NUEVO 
        #PARA TRADUCIR LOS CAMPOS QUE LE ESTOY DESIGNANDO A MI MODELO DEMO ADICIONARLE EL verbous_name EN CADA CAMPO
   










