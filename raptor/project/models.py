from django.db import models
import datetime
from django.urls import reverse


class Project(models.Model):
    """
    One to many relationship with builds
    """

    hcsec_name = models.CharField(max_length=120, primary_key=True)
    huawei_name = models.CharField(max_length=120)

    number_of_builds = models.IntegerField(default=0)
    build_attempts_successful = models.IntegerField(default=0)
    build_attempts_failed = models.IntegerField(default=0)
    build_attempts_total = models.IntegerField(default=0)

    project_active_length = models.IntegerField(default=0)  # Number of day actively working on the project
    project_active = models.BooleanField(default=False)
    project_end_date = models.DateTimeField(default=datetime.datetime.now(), blank=True)

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})  # f"/products/{self.id}/"


class Build(models.Model):
    """
    Many to one relationship with Product
    """
    product = models.ForeignKey("Project", on_delete=models.CASCADE)

    id = models.IntegerField(primary_key=True)
    build_name = models.CharField(max_length=120)

    machine_status = models.CharField(default="Not running", max_length=60)

    windows = models.BooleanField(default=False)
    windows_ip = models.TextField()

    linux = models.BooleanField(default=False)
    linux_ip = models.TextField()

    licenses_required = models.TextField(default="None")

    builds_attempted = models.IntegerField(default=0)
    build_attempts_successful = models.IntegerField(default=0)
    build_attempts_failed = models.IntegerField(default=0)

    build_notes = models.TextField()

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    previous_build_time = models.DateTimeField()

    pandas_time_frame = models.TextField()

    initial_status = models.BooleanField(default=False)
    bep_step_status = models.BooleanField(default=False)
    null_catcher_status = models.BooleanField(default=False)
    log_status = models.BooleanField(default=False)
    completeness_status = models.BooleanField(default=False)
    audit_status = models.BooleanField(default=False)
    build_monitor_status = models.BooleanField(default=False)
    semmel_status = models.BooleanField(default=False)

    bep_step_location = models.BooleanField()
    null_catcher_location = models.BooleanField()
    log_location = models.BooleanField()
    auditd_location = models.BooleanField()
    sysmon_location = models.BooleanField()
    build_monitor_location = models.BooleanField()
    semmel_location = models.BooleanField()



