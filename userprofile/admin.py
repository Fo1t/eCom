from django.contrib import admin
from django.contrib.auth import admin as upstream
#from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# class UserInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False
#     verbose_name_plural = 'Доп. информация'
#     fieldsets = (
#         (None, {
#             'fields': ('address', 'city', 'post_code')
#         }),
#     )
#
#
# #Определяем новый класс настроек для модели User
# class UserAdmin(admin.ModelAdmin):
#     inlines = (UserInline,)
#     fieldsets = (
#         (None, {'fields': ('username', 'password','email')}),
#         (('Personal info'), {'fields': ('first_name', 'last_name')}),
#         (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
#                                           'groups', 'user_permissions')}),
#         (('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'email')}
#         ),
#     )
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#
# # Перерегистрируем модель User
# try:
#     admin.site.unregister(User)
# except admin.sites.NotRegistered:
#     pass
# # admin.site.register(UserProfile)
# admin.site.register(User, UserAdmin)


