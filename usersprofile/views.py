from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from .models import CustomUser 

class RegisterViewSet(viewsets.ViewSet):
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginViewSet(viewsets.ViewSet):
    def create(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save()

class UpdateProfileViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.request.user.id)

    def perform_update(self, serializer):
        serializer.save()

    
    
# class Register(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Login(APIView):
#     def post(self, request):
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(request, email=email, password=password)
#         if user is not None:
#             login(request, user)
#             return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

# class Logout(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         logout(request)
#         return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

# class Profile(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

# class UpdateProfile(APIView):
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         serializer = UserSerializer(request.user)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request):
#         serializer = UserSerializer(request.user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Profile updated successfully'}, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

