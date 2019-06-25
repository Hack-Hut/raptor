from rest_framework import serializers

from project.models import Project, Build, Results


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "hcsec_name"
        ]


class BuildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Build
        fields = [
            "build_id", "project", "current_stage", "i_completed", "b_completed", "s_completed",
            "c_completed", "state", "M1_ip", "M2_ip"
        ]


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = [
            "build_id", "i_result_loc", "b_result_loc", "s_result_loc", "proxy_loc1", "proxy_loc2",
            "plugin_loc1", "plugin_loc2"
        ]

