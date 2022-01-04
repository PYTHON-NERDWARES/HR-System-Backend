from rest_framework import serializers
from .models import CustomUser ,Branch, Department, Leave

from django.contrib.auth.hashers import make_password
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def to_representation(self, instance):
        rep1 = super(AccountSerializer, self).to_representation(instance)
        rep1['branch'] = instance.branch.name
        rep1['department'] = instance.department.name

        return rep1


    def create(self, validated_data):
        if validated_data.get('password'):
            validated_data['password'] = make_password(validated_data['password'])
        return super(AccountSerializer, self).create(validated_data)




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

class LeaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leave
        fields = "__all__"