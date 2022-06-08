# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
# Register your models here.

User = get_user_model()


class UserAdminCustom(UserAdmin):
    # ユーザー詳細
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'name',
                'email',
                'password',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )

    # ユーザー一覧
    list_display = (
        'id',
        'name',
        'email',
        'is_active',
    )

    list_filter = ()
    # 検索
    search_fields = ('email', )
    # 順番
    ordering = ('id', )


admin.site.register(User)
