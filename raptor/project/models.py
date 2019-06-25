from django.db import models


class Project(models.Model):
    """
    One to many relationship with builds
    """

    hcsec_name = models.CharField(max_length=120, primary_key=True)


class Build(models.Model):
    """
    Many to one relationship with Product
    """
    build_id = models.IntegerField(primary_key=True)
    project = models.ForeignKey("Project", on_delete=models.CASCADE)

    current_stage = models.CharField(max_length=200)

    i_completed = models.BooleanField(default=False)
    b_completed = models.BooleanField(default=False)
    s_completed = models.BooleanField(default=False)
    c_completed = models.BooleanField(default=False)

    state = models.CharField(max_length=100)
    M1_ip = models.CharField(max_length=15)
    M2_ip = models.CharField(max_length=15)


class Results(models.Model):
    build_id = models.ForeignKey("Build", on_delete=models.CASCADE)
    i_result_loc = models.CharField(max_length=300)
    b_result_loc = models.CharField(max_length=300)
    s_result_loc = models.CharField(max_length=300)
    proxy_loc1 = models.CharField(max_length=300)
    proxy_loc2 = models.CharField(max_length=300)
    plugin_loc1 = models.CharField(max_length=300)
    plugin_loc2 = models.CharField(max_length=300)
