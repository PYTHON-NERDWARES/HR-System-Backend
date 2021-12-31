from django.urls import path
from .views import AccountList , AccountDetail ,BranchtList, BranchDetail, DepartmentList,DepartmentDetail

urlpatterns = [
    path("", AccountList.as_view(), name="account_list"),
    path("<int:pk>/", AccountDetail.as_view(), name="account_detail"),

    path("branch", BranchtList.as_view(), name="branch_list"),
    path("branch/<int:pk>/", BranchDetail.as_view(), name="branch_detail"),

    path("department", DepartmentList.as_view(), name="department_list"),
    path("department/<int:pk>/", DepartmentDetail.as_view(), name="department_detail"),
]
