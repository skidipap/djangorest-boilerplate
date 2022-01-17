from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer


class CurrentUserView(APIView):
    def get(self, request):
        if request.user.is_anonymous:
            return Response({"message": "not login", "data": ""}, status=status.HTTP_401_UNAUTHORIZED)
        serializer = UserSerializer(request.user)
        message = "succes"
        return Response({"message": message, "data": serializer.data}, status=status.HTTP_200_OK)