from django.contrib import admin

from userprofile.models import UserProfile
from .models import Manufacturer, Category, Image, Product

#from account.models import User as my_user

admin.site.register(Manufacturer)
admin.site.register(Category)
admin.site.register(Image)
#admin.site.register(Product)
#admin.site.register(TitleImage)

class ImageInLine(admin.TabularInline):
    model = Image
    #fieldsets = ('file', 'title_image',)
    fieldsets = (
        (None, {
            'fields': ('id', 'file')
        }),
    )
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'manufacturer', 'price',
                    'category', 'availability', 'weight', 'sale')
    list_filter = ('price', 'sale', 'weight', 'availability', 'category', 'manufacturer')
    inlines = [ImageInLine]


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_num']

# Register your models here.

from django.contrib.auth import admin as upstream
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import Group, User

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('city', 'address', 'post_code', 'phone')

class UserInline(admin.StackedInline):
    model = UserProfile
    #can_delete = False
    verbose_name_plural = 'Доп. информация'
    fieldsets = (
        (None, {
            'fields': ('city', 'address', 'post_code')
        }),
    )
    extra = 0

class UserAdmin(upstream.UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password','email')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'email')}
        ),
    )
    inlines = (UserInline,)
    form = UserChangeForm
    add_form = UserCreationForm
    #admin.site.unregister(User)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
#admin.site.register(TitleImage)


