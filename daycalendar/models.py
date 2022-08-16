from django.db import models

class Calendar(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateTimeField()
    tempo = models.TimeField()
    def __src__(self):
        return self.titulo
    
        