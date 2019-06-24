from django import forms
import datetime

from .models import Project


class ProjectForm(forms.ModelForm):
    hcsec_name = forms.CharField(label='HCSEC project name', widget=forms.TextInput(attrs={"placeholder": "HCSEC-"}))
    huawei_name = forms.CharField(label='Huawei delivery name', widget=forms.TextInput())

    number_of_builds = forms.IntegerField(initial=0)
    build_attempts_successful = forms.IntegerField(initial=0)
    build_attempts_failed = forms.IntegerField(initial=0)
    build_attempts_total = forms.IntegerField(initial=0)
    project_active = forms.BooleanField(initial=0)
    project_end_date = forms.DateTimeField(initial=datetime.datetime.now())

    class Meta:
        model = Project
        fields = [
            'hcsec_name',
            'huawei_name',
            'number_of_builds',
            'build_attempts_successful',
            'build_attempts_failed',
            'build_attempts_total',
            'project_active',
            'project_end_date',
        ]
