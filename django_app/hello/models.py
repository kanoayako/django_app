from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200) 
    birthday = models.DateField()
    size = models.IntegerField(default=0)
    heel = models.IntegerField(default=0)
    fvbr = models.CharField(max_length=100)
    fvshbr = models.CharField(max_length=100)
    fvclbr = models.CharField(max_length=100)
    zodata = models.CharField(max_length=100)
    appdata = models.CharField(max_length=100)
    add = models.CharField(max_length=100)
    ofadd = models.CharField(max_length=100)
    ofty = models.CharField(max_length=100)
    posi = models.CharField(max_length=100)
    out = models.CharField(max_length=100)
    pur = models.CharField(max_length=100)
    situ = models.CharField(max_length=100)

    def __str__(self):
        return '<Friend:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.fvbr) + ')>'

# Create your models here.
