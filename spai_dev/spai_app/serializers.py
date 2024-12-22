from rest_framework import serializers
from .models import LifeMembers


class LifeMembersSerializer(serializers.ModelSerializer):
    membership_date = serializers.DateField(
        format="%d-%m-%Y",  # This is the desired output format
        input_formats=["%d.%m.%Y", "%d-%m-%Y", "%Y-%m-%d", "%d.%m.%y"],
        required=False,
        allow_null=True
    )
    upload_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", required=False)
    update_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S", required=False)

    def to_internal_value(self, data):
        for key, value in data.items():
            if value == "":
                data[key] = None
        return super().to_internal_value(data)

    class Meta:
        model = LifeMembers
        fields = ['reg_no', 'name', 'address', 'mobile', 'email', 'membership_date', 'upload_date', 'update_date',
                  'active', 'uid', 'lm_key']
        read_only_fields = ['upload_date', 'update_date']
