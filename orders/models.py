from django.db import models
from users.models import Car, SalesDepartment, Manager


class Order(models.Model):
    description = models.TextField(null=True, blank=True)
    car = models.ForeignKey(
        Car,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="orders"
    )
    sales_department = models.ManyToManyField(
        SalesDepartment,
        blank=True,
        related_name="orders"
    )
    created_at = models.DateTimeField(auto_now=True)
    manager_commentary = models.TextField(null=True, blank=True)
    completed_by = models.ForeignKey(
        Manager,
        on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="completed_orders"
    )
    assigned_to = models.ForeignKey(
        Manager, on_delete=models.SET_NULL,
        blank=True, null=True,
        related_name="assigned_orders"
    )

    STATUS_CHOICES = (
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new'
    )

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"

    def __str__(self):
        client_name = self.car.owner.first_name if self.car and self.car.owner else 'No Client'
        vin_code = self.car.vin_code if self.car else 'No Car'
        return f"{self.id} - {client_name} - {vin_code}"
