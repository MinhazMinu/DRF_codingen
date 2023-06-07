from .permissions import IsStaffEditorPermissions
from rest_framework import permissions


class StaffEditorPermissionsMixin:
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermissions,
    ]
