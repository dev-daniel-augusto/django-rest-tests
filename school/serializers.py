from rest_framework import serializers
from re import search
from .models import (
                    Parent,
                    Phone,
                    Student,
                    Subject,
                    Teacher,
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
            email_split = email.split('@')
            domain = email_split[1].split('.')[0]
            if domain in email_domains:
                return email
            else:
                raise serializers.ValidationError(
                    f"You've sent an e-mail with {domain} domain which is not valid domain. "
                    f"Check the following valid domains options: " 
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


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = [
            'id',
            'subject',
            'created',
            'modified',
            'is_live',
        ]


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = [
            'id',
            'name',
            'created',
            'modified',
            'is_live',
        ]
