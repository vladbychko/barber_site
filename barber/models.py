from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "Послуга"
        verbose_name_plural = "Послуги"

    def __str__(self):
        return self.name


class Stylist(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, default="Барбер")
    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = "Майстер"
        verbose_name_plural = "Майстри"

    def __str__(self):
        return self.name


class Booking(models.Model):
    name = models.CharField("Ім'я", max_length=100)
    phone = models.CharField("Телефон", max_length=20)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField("Дата візиту")
    time = models.TimeField("Час візиту")
    message = models.TextField("Коментар", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Запис"
        verbose_name_plural = "Записи"

    def __str__(self):
        return f"{self.name} - {self.date} {self.time}"
