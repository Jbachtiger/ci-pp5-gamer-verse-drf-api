from rest_framework import generics
from pp5_gamer_verse_drf_api.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer



# DRF-API walkthrough used to get guidance on creating profile views
class ProfileList(generics.ListAPIView):
    """
    List all profiles
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


# class ProfileDetail(APIView):
#     serializer_class = ProfileSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         try:
#             profile = Profile.objects.get(pk=pk)
#             self.check_object_permissions(self.request, profile)
#             return profile
#         except Profile.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(
#             profile, context={'request': request}
#         )
#         return Response(serializer.data)

#     def put(self, request, pk):
#         profile = self.get_object(pk)
#         serializer = ProfileSerializer(
#             profile, data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

