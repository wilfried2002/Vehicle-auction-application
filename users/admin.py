from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

# Actions personnalisées
def make_sellers(modeladmin, request, queryset):
    for user in queryset:
        if not user.is_superuser:  # ne pas modifier les superadmins
            user.profile.role = 'seller'
            user.profile.save()
make_sellers.short_description = "Définir comme vendeurs"

def make_buyers(modeladmin, request, queryset):
    for user in queryset:
        if not user.is_superuser:
            user.profile.role = 'buyer'
            user.profile.save()
make_buyers.short_description = "Définir comme acheteurs"

class CustomUserAdmin(BaseUserAdmin):
    inlines = [ProfileInline]
    list_display = ('username', 'email', 'is_staff', 'is_superuser', 'get_role')
    list_filter = ('is_staff', 'is_superuser')
    actions = [make_sellers, make_buyers]

    def get_role(self, obj):
        if obj.is_superuser:
            return "superadmin"
        return obj.profile.role
    get_role.short_description = 'Rôle'

# Appliquer le nouvel admin
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
