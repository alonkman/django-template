from rest_framework import serializers
from . models import Exmpale


class Exmapleserializer(serializers.ModelSerializer):
    class Meta:
        model = Exmpale
        fields = '__all__'



# #  ---------------- with validations ----------------#
# class (your model)Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = your_model
#         fields =['amount','desc', 'price']
#     def create(self, validated_data):
#         # return your_model.objects.create(**validated_data)
#       user = self.context['user']
#       return your_model.objects.create(**validated_data, user=user)
    

