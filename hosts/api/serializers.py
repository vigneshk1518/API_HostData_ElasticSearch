from ..models import Host
# from rest_framework import serializers
from rest_framework import serializers

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ('hostname', 'hostloc') # if not declare, all fields of the model will be shown
