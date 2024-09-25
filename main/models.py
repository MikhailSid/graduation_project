from django.db import models

class InitConds(models.Model):
    date = models.DateField(default=None)
    grid = models.CharField(default=None)
    exe = models.CharField(default=None)
    log = models.TextField(default='')
    
    class Meta:
        managed = True
        db_table = 'init_conds'

class Calculations(models.Model):
    init_cond = models.ForeignKey(InitConds, on_delete=models.DO_NOTHING)
    date = models.DateField(default='2014-01-01')
    extract_step = models.CharField(default=None)
    ion_step = models.CharField(default=None)
    thermo_step = models.CharField(default=None)
    thermo_type = models.CharField(default=None)
    data_to_load = models.CharField(default=None)
    log = models.TextField(default='')
    
    class Meta:
        managed = True
        db_table = 'calculations'