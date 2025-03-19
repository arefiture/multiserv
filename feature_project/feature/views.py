from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from feature.authentication import ECAAuthentication


class ProtectedDataView(APIView):
    authentication_classes = [ECAAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            'message': f'Hello, {request.user.username}!',
            'user_id': request.user.id
        })