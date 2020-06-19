from rest_framework import serializers
from .models import *


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = '__all__'


class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'


class ProsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pro
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = ['first_name', 'last_name', 'mail', 'phone', 'type']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class BriefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brief
        fields = ['type', 'desc', 'site', 'aim', 'tasks', 'sites_pros', 'sites_cons', 'site_style',
                  'site_style_custom', 'logo', 'version', 'version_custom', 'deadline', 'first_name',
                  'last_name', 'comment', 'mail', 'phone']
