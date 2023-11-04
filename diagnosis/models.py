# diagnosis/models.py

from django.db import models
from django.contrib.auth.models import User

class Symptom(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    severity = models.PositiveIntegerField(default=1, help_text="Severity level (1-10)")

    def __str__(self):
        return self.name

class Diagnosis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    symptoms = models.ManyToManyField(Symptom)
    result = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Diagnosis for {self.user} on {self.date}"

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return f"Report for {self.user} on {self.diagnosis.date}"
