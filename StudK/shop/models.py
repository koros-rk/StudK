from django.db import models


class Photos(models.Model):
    url = models.URLField(max_length=500)


class Style(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Colour(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Material(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Handle(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Facade(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.URLField(max_length=500)
    main_photo = models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Slab(models.Model):
    title = models.CharField(max_length=100)
    thumbnail = models.URLField(max_length=500)
    main_photo = models.URLField(max_length=500)

    def __str__(self):
        return self.title


class Product(models.Model):
    # main part
    title = models.CharField(max_length=100)
    description_shorted = models.CharField(max_length=200)
    description_full = models.TextField()
    main_photo = models.URLField(max_length=500)

    # partition part
    photos = models.ManyToManyField(Photos)
    styles = models.ManyToManyField(Style)
    colours = models.ManyToManyField(Colour)
    materials = models.ManyToManyField(Material)
    facades = models.ManyToManyField(Facade)
    slabs = models.ManyToManyField(Slab)
    handle = models.ForeignKey(Handle, on_delete=models.CASCADE)

    # utility part
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    show = models.BooleanField(default=True)

    def __str__(self):
        return self.title
