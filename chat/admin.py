from django.contrib import admin
from chat.models import Room, Line

# Register your models here.
class LinesInline(admin.TabularInline):
    model = Line

class RoomAdmin(admin.ModelAdmin):
    inlines = [LinesInline]

admin.site.register(Room, RoomAdmin)
