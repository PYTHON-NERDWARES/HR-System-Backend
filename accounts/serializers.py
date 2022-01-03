from rest_framework import serializers
from .models import CustomUser ,Branch, Department
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


# class UserCreateSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, required=True, style={
#                                      "input_type":   "password"})
#     password2 = serializers.CharField(
#         style={"input_type": "password"}, write_only=True, label="Confirm password")
#     class Meta:
#         model = User
#         fields = [
#             "username",
#             "email",
#             "password",
#             "password2",
#         ]
#         extra_kwargs = {"password": {"write_only": True}}
#     def create(self, validated_data):
#         username = validated_data["username"]
#         email = validated_data["email"]
#         password = validated_data["password"]
#         password2 = validated_data["password2"]
#         if (email and User.objects.filter(email=email).exclude(username=username).exists()):
#             raise serializers.ValidationError(
#                 {"email": "Email addresses must be unique."})
#         if password != password2:
#             raise serializers.ValidationError(
#                 {"password": "The two passwords differ."})
#         user = User(username=username, email=email)
#         user.set_password(password)
#         user.save()
#         return user