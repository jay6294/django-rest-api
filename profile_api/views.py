from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profile_api import Serializer
from profile_api import models


class HelloApiViews(APIView):
    """Test Aoi view"""
    Serializer_class = Serializer.HelloSerializers

    def get(self, request, format=None):
        """return a list of api"""

        an_apiview = ["hello", "world"]

        return Response({"message": "hello", "an_apiview": an_apiview})

    def post(self, request):
        """create a hello message"""
        serializers = self.Serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get("name")
            message = f"hello{name}"
            return Response({"message": message})
        else:
            return Response(Serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, result, pk=None):
        """Put request to update object"""
        return Response({"message": "Put"})

    def patch(self, result, pk=None):
        """Patch request to partial update object"""
        return Response({"message": "Patch"})

    def delete(self, result, pk=None):
        """Delete request to delete object"""
        return Response({"message": "Delete"})


class HelloViewSets(viewsets.ViewSet):
    """test Api ViewSet"""
    serializer_class = Serializer.HelloSerializers

    def lists(self, request):
        """return a hello message"""
        vi_list = ["list", "create", "update", "partial_update", "retrieve"]
        return Response({"message": "hello", "list": vi_list})

    def create(self, request):
        """create a hello message"""
        serializer = self.Serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"my name is {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """getting obj by id"""
        return Response({"http_method", "Get or Create"})

    def update(self, request, pk=None):
        """Handle obj Updating"""
        return Response({"message": "update or put"})

    def update_partial(self, request, pk=None):
        """Handle obj partial update"""
        return Response({"message": "update_partial or patch"})

    def destroy(self, request, pk=None):
        """Delete obj from app"""
        return Response({"message": "delete or destroy"})


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = Serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
