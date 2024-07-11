from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Manager


class ManagerCreationForm(UserCreationForm):
    class Meta:
        model = Manager
        fields = (
            'username', 'first_name', 'last_name', 'email', 'phone_number',
            'sales_department'
        )


class ManagerChangeForm(UserChangeForm):
    class Meta:
        model = Manager
        fields = (
            'username', 'first_name', 'last_name', 'email', 'phone_number',
            'sales_department'
        )
