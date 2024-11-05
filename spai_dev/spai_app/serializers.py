from rest_framework import serializers
from .models import LifeMembers


class LifeMembersSerializer(serializers.ModelSerializer):
    membership_date = serializers.DateField(format="%d-%m-%Y", input_formats=["%d-%m-%Y", "%Y-%m-%d"], required=False)
    upload_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", required=False)
    update_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", required=False)

    class Meta:
        model = LifeMembers
        fields = ['name', 'address', 'mobile', 'email', 'membership_date', 'upload_date', 'update_date',
                  'is_expire']
        read_only_fields = ['upload_date', 'update_date']
