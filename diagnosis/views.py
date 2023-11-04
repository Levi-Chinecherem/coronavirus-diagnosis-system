# diagnosis/views.py

from django.shortcuts import render, redirect
from .models import Symptom, Diagnosis, Report
from .diagnostic_logic import generate_diagnosis
from .forms import DiagnosisReportForm
from chartjs.views.lines import BaseLineChartView
from django.db.models.functions import TruncDay, TruncDay, TruncHour, TruncMinute
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
import json 

def home(request):
    return render(request, 'home.html')

def diagnosis_report(request):
    if request.method == 'POST':
        form = DiagnosisReportForm(request.POST)
        if form.is_valid():
            selected_symptoms = form.cleaned_data['selected_symptoms']
            description = form.cleaned_data['description']

            # Handle diagnosis logic
            diagnosis_result = generate_diagnosis(selected_symptoms, request.user)
            # Save the diagnosis in the database
            diagnosis = Diagnosis(user=request.user, result=diagnosis_result)
            diagnosis.save()

            # Check if the user provided a description
            if description:
                # Handle report logic
                report = Report(user=request.user, diagnosis=diagnosis, description=description)
                report.save()

            return redirect('diagnosis:diagnosis_result', diagnosis_id=diagnosis.id)
    else:
        form = DiagnosisReportForm()

    return render(request, 'diagnosis/diagnosis_report.html', {'form': form})

def diagnosis_result(request, diagnosis_id):
    # Get the diagnosis object if it belongs to the logged-in user
    diagnosis = Diagnosis.objects.filter(id=diagnosis_id, user=request.user).first()

    if not diagnosis:
        # Handle the case where the diagnosis does not exist or does not belong to the user
        return redirect('diagnosis:home')  # Redirect to an appropriate page

    return render(request, 'diagnosis/diagnosis_result.html', {'diagnosis': diagnosis})

def diagnosis_list(request):
    # Get a list of diagnoses belonging to the logged-in user
    diagnoses = Diagnosis.objects.filter(user=request.user)
    return render(request, 'diagnosis/diagnosis_list.html', {'diagnoses': diagnoses})

def report_list(request):
    # Get a list of reports belonging to the logged-in user
    reports = Report.objects.filter(user=request.user)
    return render(request, 'diagnosis/report_list.html', {'reports': reports})


class LiveReportView(LoginRequiredMixin, BaseLineChartView):
    chart_type = 'bar'

    def get_labels(self):
        labels = Diagnosis.objects.filter(user=self.request.user).annotate(
            day=TruncDay('date')
        ).values('day').distinct()
        formatted_labels = [label['day'].strftime('%d %b %Y') for label in labels]
        return formatted_labels

    def get_data(self):
        formatted_labels = self.get_labels()
        symptoms_count = Diagnosis.objects.filter(user=self.request.user).annotate(
            day=TruncDay('date')
        ).filter(day__isnull=False).values('day').annotate(count=Count('id')).order_by('day')
        diagnosis_count = Diagnosis.objects.filter(user=self.request.user).annotate(
            day=TruncDay('date')
        ).filter(day__isnull=False).values('day').annotate(count=Count('id')).order_by('day')

        symptoms_dict = {item['day'].strftime('%d %b %Y'): item['count'] for item in symptoms_count}
        diagnosis_dict = {item['day'].strftime('%d %b %Y'): item['count'] for item in diagnosis_count}

        symptoms_data = [symptoms_dict.get(label, 0) for label in formatted_labels]
        diagnosis_data = [diagnosis_dict.get(label, 0) for label in formatted_labels]

        return [symptoms_data, diagnosis_data]

    def get_datasets(self):
        symptoms_data, diagnosis_data = self.get_data()
        datasets = [
            {
                'label': 'Symptoms Reports',
                'data': symptoms_data,
                'borderColor': 'rgba(255, 99, 132, 1)',
                'backgroundColor': 'rgba(255, 0, 132, 0.6)',  # Background color for the bars
            },
            {
                'label': 'Diagnosis Reports',
                'data': diagnosis_data,
                'borderColor': 'rgba(75, 192, 192, 1)',
                'backgroundColor': 'rgba(175, 32, 0, 0.6)',
            },
        ]
        return datasets

    def get(self, request, *args, **kwargs):
        labels = self.get_labels()
        datasets = self.get_datasets()
        datasets_json = json.dumps(datasets)
        return render(request, 'diagnosis/live_report.html', {'labels': labels, 'datasets': datasets_json, 'chart_type': self.chart_type})
