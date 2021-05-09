from rest_framework import serializers
from re import search
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

    def validate_email(self, email):
        email_domains = ['gmail', 'yahoo', 'hotmail', 'aol', 'msn', 'wanadoo',
                         'live', 'rediffmail', 'free', 'gmx']
        if search('@', email):
            first = email.split('@')
            second = first[1].split('.')
            if second[0] in email_domains:
                return email
            else:
                raise serializers.ValidationError(
                f"You've sent {second[0]} domain which is not valid domain. "
                f"Check the following valid domains options:" 
                f"gmail, yahoo, hotmail, aol, msn, wanadoo, live, rediffmail, free, gmx")
        else:
            pass


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
