from rest_framework import serializers
from .models import CustomUser ,Branch, Department


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def to_representation(self, instance):
        rep1 = super(AccountSerializer, self).to_representation(instance)
        rep1['branch'] = instance.branch.name
        rep1['department'] = instance.department.name

        return rep1


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

    def to_representation(self, instance):
        rep1 = super(DepartmentSerializer, self).to_representation(instance)
        rep1['branch'] = instance.branch.name

        return rep1