from django.shortcuts import render

from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CustomUser, Branch, Department
from .permissions import IsOwnerOrReadOnly, IsOwnerOrReadOnly_for_Branch_and_department
from .serializers import AccountSerializer, BranchSerializer, DepartmentSerializer


class AccountList(ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer
    


class AccountDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = AccountSerializer


####################################################################
class BranchtList(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer
    

class BranchDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly_for_Branch_and_department,)
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


#####################################################################
class DepartmentList(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DepartmentDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly_for_Branch_and_department,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer