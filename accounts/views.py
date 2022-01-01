from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CustomUser, Branch, Department
from .permissions import IsHROrEmployee
from .serializers import AccountSerializer, BranchSerializer, DepartmentSerializer


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
