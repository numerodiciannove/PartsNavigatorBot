from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import Manager, Client, SalesDepartment, Car
from .forms import ManagerCreationForm, ManagerChangeForm


@admin.register(Manager)
class ManagerAdmin(UserAdmin):
    add_form = ManagerCreationForm
    form = ManagerChangeForm
    model = Manager
    list_display = (
        'username', 'first_name', 'last_name', 'phone_number', 'id')
    search_fields = ('id', 'first_name', 'last_name', 'phone_number')
    filter_horizontal = ('sales_department',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info',
         {'fields': ('first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups',
            'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Sales Department', {'fields': ('sales_department',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'password1', 'password2', 'first_name',
                'last_name',
                'email', 'phone_number', 'sales_department')}
         ),
    )


class CarInline(admin.TabularInline):
    model = Car
    extra = 1


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'phone_number',
        'first_name',
        'telegram_id',
        'telegram_username',
        'created_at',
        "id",
    )
    search_fields = (
        'first_name',
        'phone_number',
        'telegram_username',
    )
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
    inlines = [CarInline]


class CarAdmin(admin.ModelAdmin):
    list_display = (
        'vin_code',
        'owner_link',
        'brand',
        'model',
        'color',
        'registration_number',
        'id',
    )
    list_filter = ('brand', 'color')
    search_fields = ('brand', 'model', 'vin_code', 'registration_number')

    def owner_link(self, obj):
        owner = obj.owner
        if owner:
            return mark_safe(owner.get_link())
        return "-"

    owner_link.short_description = 'Owner'


admin.site.register(Car, CarAdmin)


@admin.register(SalesDepartment)
class SalesDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)
    search_fields = ('name', 'id',)
