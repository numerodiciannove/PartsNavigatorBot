from django.contrib.auth.models import AbstractUser
from django.db import models


class SalesDepartment(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )

    class Meta:
        ordering = [
            "name",
        ]

    def __str__(self):
        return f"{self.id} - {self.name}"


class Manager(AbstractUser):
    sales_department = models.ManyToManyField(
        SalesDepartment,
        blank=True,
        related_name="managers"
    )
    phone_number = models.CharField(
        blank=True,
        null=True,
        max_length=13
    )

    def __str__(self):
        return f"{self.username}"


class Client(models.Model):
    first_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=13,
        null=True,
        blank=True
    )
    telegram_id = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    telegram_username = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def get_link(self):
        return f'<a href="/admin/users/client/{self.pk}/">{self.first_name}</a>'

    def __str__(self):
        return f"ID#{self.id} - {self.first_name}"


class Car(models.Model):
    owner = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='cars'
    )
    vin_code = models.CharField(
        max_length=17,
        null=True,
        blank=True
    )
    brand = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    registration_number = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"VIN - {self.vin_code} - {self.owner.first_name}  📞{self.owner.phone_number}"
