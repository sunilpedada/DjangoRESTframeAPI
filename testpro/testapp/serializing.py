from rest_framework import serializers
from.models import EmployeDetails
def multipels_of_1000(value):
    if value%1000!=0:
        raise serializers.ValidationError("should be multipel of 1000")
class EmployeSerializer(serializers.Serializer):
    ename=serializers.CharField(max_length=10)# inbuilt validators
    email=serializers.EmailField()
    esalary=serializers.IntegerField(validators=[multipels_of_1000,])
    def validate_esalary(self,value):# field level validation
        if value>5000:
            raise serializers.ValidationError("employe salary should be less then 5000")
        return value
    def validate(self,data):# OBJECT LEVEL VALIDATION
        ename=data.get("ename")
        esalary=data.get("esalary")
        if ename=="hari":
            if esalary>20:
                raise serializers.ValidationError("hi hari your salary should be less then 20")
        return data
    def create(self,validated_data):
        return EmployeDetails.objects.create(**validated_data)
    def update(self,instance,validated_data):
        instance.ename=validated_data.get("ename",instance.ename)
        instance.email=validated_data.get("email",instance.email)
        instance.esalary=validated_data.get("esalary",instance.esalary)
        instance.save()
        return instance
# //////////// ModelSerializer////////////////////////////////////
class EmployeModelSerializer(serializers.ModelSerializer):
    esalary=serializers.IntegerField(validators=[multipels_of_1000,])
    class Meta:
        model=EmployeDetails
        #fields="__all__"
        fields=["ename","esalary"]
        #exclude=["esalary"]
    def validate_esalary(self,value):# field level validation
        if value>5000:
            raise serializers.ValidationError("employe salary should be less then 5000")
        return value
    def validate(self,data):# OBJECT LEVEL VALIDATION
        ename=data.get("ename")
        esalary=data.get("esalary")
        if ename=="hari":
            if esalary>20:
                raise serializers.ValidationError("hi hari your salary should be less then 20")
        return data
class testserializer(serializers.Serializer):
    name=serializers.CharField(max_length=10)
    