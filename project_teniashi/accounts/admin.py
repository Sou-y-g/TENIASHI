from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

#admin画面の変更 list_displayは画面の中央の値
class UserAdmin(BaseUserAdmin):
    list_display = (
        "email",
        "username",
    )

#上で定義したadmin画面の変更を適用する
admin.site.register(User, UserAdmin)
