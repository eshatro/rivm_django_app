from django.db import models


class Geography(models.Model):
    id = models.CharField(max_length=2, unique=True, primary_key=True)
    short_name = models.CharField(max_length=3, null=True, blank=True)
    name = models.CharField(max_length=125, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Geographies'

    def __str__(self):
        return self.name


class DataSource(models.Model):
    data_source_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'DataStores'

    def __str__(self):
        return self.data_source_name


class Entry(models.Model):
    product_name = models.CharField(max_length=255, null=True, blank=True)
    unit = models.CharField(max_length=45, null=True, blank=True)
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE)
    data_source = models.ForeignKey(DataSource, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self):
        return f"{self.product_name, self.unit}"


class Indicator(models.Model):
    method = models.CharField(max_length=45, null=True, blank=True)
    category = models.CharField(max_length=45, null=True, blank=True)
    indicator = models.CharField(max_length=45, null=True, blank=True)
    unit = models.CharField(max_length=45, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Indicators'

    def __str__(self):
        return f"{self.method, self.category, self.indicator, self.unit}"


class Impact(models.Model):
    indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    coefficient = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Impacts'

    def __str__(self):
        return f"{self.coefficient}"
