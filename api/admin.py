from django.contrib import admin
from .models import UserModel,DataModel,ContactData
from django.contrib.auth.admin import UserAdmin


class UserAdminConfig(UserAdmin):
    model = UserModel
    search_fields = ('email', 'username', 'firstname',)
    list_filter = ('email', 'username', 'firstname', 'is_active', 'is_staff')
    ordering = ('start_date',)
    list_display = ('email', 'username', 'firstname',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username',)}),
        ('Personal', {'fields': ( 'firstname','lastname','mobile','dp','age','gender','about',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','groups','user_permissions','is_superuser','last_login','start_date',)}),
    )
    # formfield_overrides = {
    #     NewUser.about: {'widget': Textarea(attrs={'rows': 10, 'cols': 5})},
    # }
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'firstname','lastname','mobile','dp','age','gender','about', 'password1', 'password2', 'is_active', 'is_staff')}
         ),
    )


admin.site.register(UserModel, UserAdminConfig)
admin.site.register(DataModel)
admin.site.register(ContactData)
