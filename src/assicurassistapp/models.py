from django.db import models
from django.conf import settings


class Cliente(models.Model):
    # id utente collegato a user di django
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name="clienti")
    codice_fiscale = models.CharField(max_length=100, primary_key=True)
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank = True, null = True)
    telefono = models.CharField(max_length=100)
    indirizzo = models.CharField(max_length=100, blank = True, null = True)
    citta = models.CharField(max_length=100, blank = True, null = True)
    cap = models.CharField(max_length=100 , blank = True, null = True)
    provincia = models.CharField(max_length=100, blank = True, null = True)
    data_nascita = models.DateField(blank=True, null=True)
    ultima_notifica = models.DateField(null=True, blank=True)
    comunicazioni = models.BooleanField(default=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Clienti"
    

    def __str__(self):
        return self.nome + " " + self.cognome + " - CF: " + self.codice_fiscale
    

class Veicolo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)
    targa = models.CharField(max_length=100,primary_key=True)
    marca = models.CharField(max_length=100)
    modello = models.CharField(max_length=100)
    cilindrata = models.CharField(max_length=100 , blank = True, null = True)
    alimentazione = models.CharField(max_length=100, blank = True, null = True)
    anno_immatricolazione = models.DateField(blank=True, null=True)
    assicurato = models.BooleanField(default=False)
    proprietario = models.ForeignKey(Cliente, on_delete=models.CASCADE,blank=False,null=False, related_name = 'veicoli')
    class Meta:
        verbose_name_plural = "Veicoli"


    def __str__(self):
        return self.targa


class Broker(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)
    #id_broker = models.AutoField(primary_key=True)
    nome = models.CharField(primary_key = True, max_length=100)
    note = models.TextField(blank=True,null=True)
    class Meta:
        verbose_name_plural = "Broker"


    def __str__(self):
        return self.nome

    
class Compagnia(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)
    #id_compagnia = models.AutoField(primary_key=True)
    nome = models.CharField(primary_key = True, max_length=100)
    broker = models.ForeignKey(Broker, on_delete=models.CASCADE,null=True,blank = True,related_name='broker')
    telefono = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    sito_web = models.CharField(max_length=100,blank=True,null=True)

    class Meta:
        verbose_name_plural = "Compagnie"

    def __str__(self):
        return self.nome
    

    
class Polizza(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)
    id_polizza = models.CharField(max_length=100,primary_key=True)
    compagnia = models.ForeignKey(Compagnia, on_delete=models.CASCADE,null=True,related_name='compagnia')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE,related_name='cliente')
    note = models.CharField(max_length=200,null=True,blank=True)
    semestrale = models.BooleanField(default=False)
    data_inizio = models.DateField()
    data_fine = models.DateField()
    data_fine_due = models.DateField(null=True,blank=True)
    premio = models.FloatField(blank=True,null=True)
    veicolo = models.OneToOneField(Veicolo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Polizze"

    def __str__(self):
        return self.id_polizza
    

class Documento(models.Model):
    polizza = models.ForeignKey('Polizza', on_delete=models.CASCADE, related_name='documenti')
    file = models.FileField(upload_to='documenti_polizza/', default="", null=True, blank=True)

    def __str__(self):
        return self.file.name



class Sinistro(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=False)
    id_sinistro = models.CharField(max_length=100)
    targa = models.ForeignKey(Veicolo, on_delete=models.CASCADE)
    #polizza = models.ForeignKey(Polizza, on_delete=models.CASCADE)
    data = models.DateField()
    descrizione = models.CharField(max_length=200,blank=True,null=True)
    stato = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Sinistri"

    def __str__(self):
        return self.id_sinistro