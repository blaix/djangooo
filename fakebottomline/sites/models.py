from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=100)

    @classmethod
    def create(cls, name):
        site = cls(name=name)
        site.save()
        return site

    @classmethod
    def delete_all(cls):
        cls.objects.all().delete()

    @classmethod
    def get_all(cls):
        return list(cls.objects.all())

    def __repr__(self):
        return self.name
