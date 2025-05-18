from django.contrib import admin
from .models import GlucoseReading

# Register the GlucoseReading model
@admin.register(GlucoseReading)
class GlucoseReadingAdmin(admin.ModelAdmin):
    list_display = ('user', 'glucose_level', 'timestamp')  # Fields to show in the admin list view
    list_filter = ('user', 'timestamp')  # Filters on the right
    search_fields = ('user__username',)  # Search bar for the user
