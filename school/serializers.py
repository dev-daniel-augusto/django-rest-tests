from rest_framework import serializers
from .models import (
                    Parent,
                    Phone,
                    Student,
                    )


class ParentSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Parent
        fields = [
            'id',
            'parent_name',
            'email'
        ]


class PhoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Phone
        fields = [
            'id',
            'parent_name',
            'mobile_phone',
            'landline_phone'
        ]


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Student
        fields = [
            'id',
            'parent_name',
            'student_name',
            'email',
        ]
