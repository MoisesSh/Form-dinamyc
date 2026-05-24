from django.db import models

class TrazaExterno(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    user_email = models.CharField(max_length=254, blank=True, null=True)
    action = models.CharField(max_length=100)
    entity_type = models.CharField(max_length=50)
    entity_id = models.IntegerField()
    description = models.TextField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = '"traza"."traza_externo"'



class TrazaInterno(models.Model):
    id = models.UUIDField(primary_key=True)
    user_id = models.IntegerField()
    user_email = models.CharField(max_length=254)
    role = models.CharField(max_length=20)
    action = models.CharField(max_length=50)
    entity_type = models.CharField(max_length=20)
    entity_id = models.IntegerField()
    previous_state = models.TextField(blank=True, null=True)
    new_state = models.TextField(blank=True, null=True)
    description = models.TextField()
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = '"traza"."traza_interno"'
