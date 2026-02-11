from rest_framework import serializers 

class RegistrationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only = True)
    name = serializers.CharField(
        max_length = 100,
        error_messages = {
            'required': 'Name is required',
            'blank': 'Name is required'
        }
    )