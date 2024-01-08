from .models import User,Project
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password', 'profile_picture', 'stack']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ProjectWithUserSerializer(serializers.ModelSerializer):
    students = UserSerializer(many=True,read_only=True)
    class Meta:
        model= Project
        fields = ['id','project_name','area','course','created_date','description','techs','contact','finish_ratio','status','image','price','proposal','outside_scope_items','requirements','students']


class UserWithProjectsSerializer(serializers.ModelSerializer):
    projects = ProjectSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id','username','profile_picture', 'stack','projects']