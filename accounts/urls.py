from django.urls import path
from .views import (
    AccountList,
    AccountRetrieve,
    AccountCreate,
    AccountDetail,
    BranchtList,
    BranchRetrieve,
    BranchCreate,
    BranchDetail,
    DepartmentList,
    DepartmentRetrieve,
    DepartmentCreate,
    DepartmentDetail,
    LeaveDetail,
    LeaveList,
)

urlpatterns = [
    path("", AccountList.as_view()),
    path("<int:pk>/", AccountRetrieve.as_view()),
    path("create-account", AccountCreate.as_view()),
    path("<int:pk>/update-delete/", AccountDetail.as_view()),


    path("branch", BranchtList.as_view()),
    path("branch/<int:pk>/", BranchRetrieve.as_view()),
    path("create-branch", BranchCreate.as_view()),
    path("branch/<int:pk>/update-delete/", BranchDetail.as_view()),


    path("department", DepartmentList.as_view()),
    path("department/<int:pk>/", DepartmentRetrieve.as_view()),
    path("create-department", DepartmentCreate.as_view()),
    path("department/<int:pk>/update-delete/", DepartmentDetail.as_view()),

    path("leave", LeaveList.as_view()),
    path("<int:pk>/leaveDetail", LeaveDetail.as_view())



]