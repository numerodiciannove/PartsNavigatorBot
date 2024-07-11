from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "client_name",
        "client_phone_number",
        "get_vin_code",
        "created_at",
        "get_sales_departments",
        "status",
        "assigned_to_name",
        "completed_by_name"
    )
    search_fields = ("car__owner__first_name", "description")
    list_filter = ("sales_department", "status", "assigned_to", "completed_by")
    filter_horizontal = ("sales_department",)
    date_hierarchy = "created_at"
    readonly_fields = ('description', 'completed_by', 'assigned_to')

    fieldsets = (
        (None, {
            'fields': (
                'car',
                'description',
                'manager_commentary',
                'status',
                'assigned_to',
                'completed_by'
            )
        }),
        ('Sales department', {
            'classes': ('collapse',),
            'fields': ('sales_department',),
        }),
    )

    def client_name(self, obj):
        return obj.car.owner.first_name if obj.car and obj.car.owner else None

    client_name.short_description = "Client Name"

    def client_phone_number(self, obj):
        return obj.car.owner.phone_number if obj.car and obj.car.owner else None

    client_phone_number.short_description = "Client Phone Number"

    def get_vin_code(self, obj):
        return obj.car.vin_code if obj.car else None

    get_vin_code.short_description = "VIN Code"

    def get_sales_departments(self, obj):
        return ", ".join([dep.name for dep in obj.sales_department.all()])

    get_sales_departments.short_description = "Sales Departments"

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.created_by = request.user
        elif obj.status == 'completed' and not obj.completed_by:
            obj.completed_by = request.user
        super().save_model(request, obj, form, change)

    def assigned_to_name(self, obj):
        return obj.assigned_to.username if obj.assigned_to else None

    assigned_to_name.short_description = "Assigned To"

    def completed_by_name(self, obj):
        return obj.completed_by.first_name if obj.completed_by else None

    completed_by_name.short_description = "Completed By"

    def take_order(self, request, queryset):
        updated_count = queryset.update(
            assigned_to=request.user, status='in_progress'
        )
        self.message_user(
            request,
            f"{updated_count} orders were successfully taken into work."
        )

    take_order.short_description = "🔁Take selected orders into work"

    def cancel_order(self, request, queryset):
        updated_count = queryset.update(assigned_to=None, status='new')
        self.message_user(
            request,
            f"{updated_count} orders were successfully cancelled."
        )

    cancel_order.short_description = "❌Cancel selected orders"

    def mark_as_completed(self, request, queryset):
        updated_count = queryset.update(status='completed',
                                        completed_by=request.user)
        self.message_user(
            request,
            f"{updated_count} orders were successfully marked as completed."
        )

    mark_as_completed.short_description = "✅Mark selected orders as completed"

    def mark_as_uncompleted(self, request, queryset):
        updated_count = queryset.update(
            status='completed',
            completed_by=None
        )
        self.message_user(
            request,
            f"{updated_count} orders were successfully marked as uncompleted."
        )

    mark_as_uncompleted.short_description = (
        "❌Mark selected orders as uncompleted"
    )

    actions = [
        'take_order',
        'cancel_order',
        'mark_as_completed',
        "mark_as_uncompleted",
    ]
