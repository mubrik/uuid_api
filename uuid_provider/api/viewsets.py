from rest_framework.views import APIView
from rest_framework.response import Response
from uuid_provider.models import UidGenerator
from .serializers import UidSerializer
from rest_framework import generics


class ListUuidsViewset(APIView):
    """
    simple api view class to return response of serialized object
    """

    def get(self, request):
        UidGenerator.objects.create()
        response_obj = {
            uuid.created.strftime('%Y-%m-%d %I:%M:%S.%f'): str(uuid.id)
            for uuid in UidGenerator.objects.all().order_by('-created')
        }
        return Response(response_obj)

    def post(self, request):
        """ not required but incase a single new id is needed """

        instance = UidGenerator.objects.create()
        serialized_data = UidSerializer(instance)
        return(Response(serialized_data.data))


""" class ListUuidsViewset(generics.ListCreateAPIView):

    queryset = UidGenerator.objects.all().order_by('-created')
    serializer_class = UidSerializer """
