from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CustomUser, Branch, Department
from .permissions import IsHROrEmployee
from .serializers import AccountSerializer, BranchSerializer, DepartmentSerializer , LeaveSerializer
from django.http import HttpResponse 
import json
from .models import (CustomUser , Leave)
from rest_framework.response import Response 
from rest_framework import status
# from rest_framework import detail_route

class AccountList(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer


class AccountRetrieve(RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer


class AccountCreate(CreateAPIView):
    permission_classes = (IsHROrEmployee,)
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer

    # @detail_route(methods=['post'])
    # def upload_docs(request):
        
    #     file = request.data['file']
    
    #     product = CustomUser.objects.create(Personal_Picture=file)

    # def post(self, request, format=None):
    #     serializer = AccountSerializer(data=request.data)   
    #     file = request.data['file']
    #     image = CustomUser.objects.create(image=file)     
    #     if serializer.is_valid():           
    #         serializer.save(Personal_Picture=request.data.get('Personal_Picture'))
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def post(self, request, *args, **kwargs):
    #     file = request.data['file']
    #     image = CustomUser.objects.create(image=file)
    #     return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)


    

# class RegistrationViewSet(viewsets.ModelViewSet):
#     permission_classes = (permissions.AllowAny,)
#     queryset = User.objects.all()
#     serializer_class = UserCreateSerializer
#     def get(request, pk, format=None, *args, **kwargs):
#         serializer = UserCreateSerializer(data=request.data)
#         if not serializer.is_valid():
#             return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         res = {
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#         }
#         return response.Response(res, status.HTTP_201_CREATED)


class AccountDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsHROrEmployee,)
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer


#######################################################################################
class BranchtList(ListAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchRetrieve(RetrieveAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchCreate(CreateAPIView):
    permission_classes = (IsHROrEmployee,)
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


class BranchDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsHROrEmployee,)
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


#######################################################################################
class DepartmentList(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentRetrieve(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentCreate(CreateAPIView):
    permission_classes = (IsHROrEmployee,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class DepartmentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsHROrEmployee,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class LeaveList(ListCreateAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class LeaveDetail(RetrieveUpdateDestroyAPIView):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer