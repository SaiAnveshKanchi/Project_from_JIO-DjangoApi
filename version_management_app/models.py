

from ensurepip import version
import re
from djongo import models

# Create your models here.
class Version(models.Model):
    _id = models.ObjectIdField()
    vv = models.CharField(max_length=128,unique=True)

    def __str__(self):
        return self.vv


class Device(models.Model):
    _id = models.ObjectIdField()
    dd = models.CharField(max_length=128,unique=True)

    def __str__(self):
        return self.dd


class SensorValues(models.Model):
    tm = models.CharField(max_length=128)
    hm = models.CharField(max_length=128)
    pp = models.CharField(max_length=128)
    wd = models.CharField(max_length=128)
    ws = models.CharField(max_length=128)
    sm = models.CharField(max_length=128)
    st = models.CharField(max_length=128)
    sc = models.CharField(max_length=128)
    lt = models.CharField(max_length=128)
    lw = models.CharField(max_length=128)
    bl = models.CharField(max_length=128)
    pv = models.CharField(max_length=128)

    class Meta:
        abstract = True



class Data(models.Model):
    _id = models.ObjectIdField()
    ep = models.CharField(max_length=128)
    sent_date = models.DateField()
    version = models.ForeignKey(Version,related_name="data",on_delete=models.CASCADE)
    device = models.ForeignKey(Device,related_name="data",on_delete=models.CASCADE)
    dt = models.EmbeddedField(
        model_container=SensorValues
    )
    objects = models.DjongoManager()

    class Meta:
        ordering = ["sent_date"]

    def __str__(self):
        return self.ep


class VersionAbstract(models.Model):
    version = models.CharField(max_length=128)
    no = models.IntegerField()

    class Meta:
        abstract = True


class DateSent(models.Model):
    _id = models.ObjectIdField()
    date = models.DateField(unique=True)
    versions = models.ArrayField( model_container=VersionAbstract,)
    noof_versions = models.IntegerField()
    objects = models.DjongoManager()

    def __str__(self):
        return f"{self.date}"