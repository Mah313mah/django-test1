from django.db import models


class Mod_mess(models.Model):
    test = models.CharField(max_length=225)

    def __str__(self):
        return self.test
