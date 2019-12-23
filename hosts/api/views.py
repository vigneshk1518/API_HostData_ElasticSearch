from ..models import Host
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


class HostListView(generics.ListAPIView):
    queryset = Host.objects.all()
    serializer_class = serializers.HostSerializer


class HostCreateView(generics.CreateAPIView):
    queryset = Host.objects.all()
    serializer_class = serializers.HostSerializer

    def create(self, request, *args, **kwargs):
        super(HostCreateView, self).create(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully created",
                    "result": request.data}
        return Response(response)


class HostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Host.objects.all()
    serializer_class = serializers.HostSerializer
    def retrieve(self, request, *args, **kwargs):
        super(HostDetailView, self).retrieve(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully retrieved",
                    "result": data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(HostDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully updated",
                    "result": data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(HostDetailView, self).delete(request, args, kwargs)
        response = {"status_code": status.HTTP_200_OK,
                    "message": "Successfully deleted"}
        return Response(response)
