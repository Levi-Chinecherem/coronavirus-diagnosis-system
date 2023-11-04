from django.contrib import admin
from .models import Symptom, Diagnosis, Report

class SymptomAdmin(admin.ModelAdmin):
    list_display = ('name', 'severity')
    list_filter = ('severity',)
    search_fields = ('name', 'description')

class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'result')
    list_filter = ('date',)
    search_fields = ('user__username', 'result')

class ReportAdmin(admin.ModelAdmin):
    list_display = ('user', 'diagnosis', 'description')
    list_filter = ('diagnosis__date',)
    search_fields = ('user__username', 'description')

admin.site.register(Symptom, SymptomAdmin)
admin.site.register(Diagnosis, DiagnosisAdmin)
admin.site.register(Report, ReportAdmin)
