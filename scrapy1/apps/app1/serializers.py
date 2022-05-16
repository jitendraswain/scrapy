from pyexpat import model
from rest_framework import serializers
from apps.app1.models import Covid
class SocialRegistrationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Covid
        fields = "__all__"
