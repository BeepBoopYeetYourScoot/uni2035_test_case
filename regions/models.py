from django.db import models


class Region(models.Model):
    REGION_SPECIALTIES = (
        ('AGR', 'Аграрный'),
        ('IND', 'Индустриальный'),
        ('MIN', 'Горно-добывающий'),
        ('MAN', 'Обрабатываюший'),
        ('TOU', 'Туристический'),

    )
    name = models.CharField(max_length=255)
    population = models.IntegerField(null=True, blank=True)
    main_specialty = models.CharField(max_length=64, choices=REGION_SPECIALTIES)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'regions'
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'


class City(models.Model):
    region = models.ForeignKey(Region, related_name='cities', on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    population = models.IntegerField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'cities'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        unique_together = [['region', 'name']]
