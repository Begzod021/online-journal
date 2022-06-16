from django.contrib import admin
from .models import *
from .forms import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    list_display = ['username', 'email', 'role', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('role', 'approve')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('role','approve')}),
    )


@admin.register(Teacher)
class PupilAdmin(admin.ModelAdmin):
    exclude = ['last_login', 'date_joined', 'class_number']
    add_form = TeacherCreationForm


admin.site.register(Pupil)
admin.site.register(Parent)