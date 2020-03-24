from rest_framework import serializers
class EmployeSerializer(serializers.Serializer):
    ename=serializers.CharField(max_length=10)
    email=serializers.EmailField()
    esalary=serializers.IntegerField()