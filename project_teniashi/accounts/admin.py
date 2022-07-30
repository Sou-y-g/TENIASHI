from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

#admin画面の変更 list_displayは画面の中央の値
class UserAdmin(BaseUserAdmin):
    list_display = (
        "username",
        "email",
        "is_active",
        "is_staff",
    )

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff','is_active',)}), #管理画面で権限変更をできるようにする
    )


    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2')}
        ),
    )

    list_filter = ('username', )
    search_fields = ('username', )
    ordering = ("username",)        #絞り込み
    filter_horizontal = ()          #使わない
 

#上で定義したadmin画面の変更を適用する
admin.site.register(User, UserAdmin)
