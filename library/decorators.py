from django.core.exceptions import PermissionDenied

def librarian_or_admin_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.user_type == 'librarian' or request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return _wrapped_view_func

def student_required(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if request.user.user_type == 'student':
            return view_func(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return _wrapped_view_func
