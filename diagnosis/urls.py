from django.urls import path
from . import views
from .views import LiveReportView

app_name = 'diagnosis'

urlpatterns = [
    path('', views.home, name='home'),
    path('questionnaire/', views.diagnosis_report, name='diagnosis_report'),
    path('result/<int:diagnosis_id>/', views.diagnosis_result, name='diagnosis_result'),
    path('diagnosis_list/', views.diagnosis_list, name='diagnosis_list'),
    path('report_list/', views.report_list, name='report_list'),
    path('live_report/', LiveReportView.as_view(), name='live_report'),
]
