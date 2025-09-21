from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from .serializers import InputSerializer

class BajajAPIView(APIView):
    def get(self, request):
        return Response({"operation_code": "OP12345"}, status=http_status.HTTP_200_OK)

    def post(self, request):
        # If POST body is completely empty, pass None to serializer
        data = request.data
        if not data or data == {}:   # handle empty dict or None
            data = None

        serializer = InputSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data

        highest_alphabet = max(validated_data['alphabets'])

        response_data = {
            "status": validated_data['status'],
            "user_id": validated_data['user_id'],
            "college_email": validated_data['college_email'],
            "college_roll_no": validated_data['college_roll_no'],
            "numbers": validated_data['numbers'],
            "alphabets": validated_data['alphabets'],
            "highest_alphabet": highest_alphabet
        }

        return Response(response_data, status=http_status.HTTP_200_OK)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as http_status
from .serializers import InputSerializer

class BajajAPIView(APIView):

    def get(self, request):
        return Response({"operation_code": "OP12345"}, status=http_status.HTTP_200_OK)

    def post(self, request):
        # If POST body completely empty, return default data
        if not request.body or request.body == b'':
            default_data = {
                "status": "active",
                "user_id": 101,
                "college_email": "nitesh@uit.edu",
                "college_roll_no": "UIT123",
                "numbers": [1,2,3,4],
                "alphabets": ["a","b","c"],
                "highest_alphabet": "c"
            }
            return Response(default_data, status=http_status.HTTP_200_OK)

        # Otherwise validate using serializer
        serializer = InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        data["highest_alphabet"] = max(data['alphabets'])

        return Response(data, status=http_status.HTTP_200_OK)
