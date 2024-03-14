from django.contrib import admin

from demo_test.models import Stage


# Register your models here.
@admin.register(Stage)
class StageAdmin(admin.ModelAdmin):
    pass
