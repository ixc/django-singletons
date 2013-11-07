from django.db import models

class SingletonModel(models.Model):
    
    class Meta:
        abstract = True
            
    def save(self, *args, **kwargs):
        super(SingletonModel, self).save(*args, **kwargs)