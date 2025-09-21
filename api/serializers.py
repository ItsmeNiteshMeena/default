from rest_framework import serializers

class InputSerializer(serializers.Serializer):
    status = serializers.CharField(default="active", required=False)
    user_id = serializers.IntegerField(default=101, required=False)
    college_email = serializers.EmailField(default="neeteshmaran0123@gmail.com", required=False)
    college_roll_no = serializers.CharField(default="0101CS221087", required=False)
    numbers = serializers.ListField(
        child=serializers.IntegerField(), default=[1,2,3,4], required=False
    )
    alphabets = serializers.ListField(
        child=serializers.CharField(max_length=1), default=["a","b","c"], required=False
    )


