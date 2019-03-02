from django.contrib import admin

from .models import Event, Transaction


class EventAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "description",
        "location",
        "people_involved",
        "owner",
        "date_created",
        "date_updated",
    ]
    readonly_fields = [
        "owner",
        "date_created",
        "date_updated",
    ]

    def save_model(self, request, obj, form, change):
        if not hasattr(obj, "owner"):
            obj.owner = request.user
        obj.save()


admin.site.register(Event, EventAdmin)
admin.site.register(Transaction)
