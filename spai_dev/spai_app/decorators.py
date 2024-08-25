from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def authenticated_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return view_func(request, *args, **kwargs)
        return redirect('login_page')
    return wrapper


def common_user_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_role == 2 and request.user.admin_approved:
            return view_func(request, *args, **kwargs)
        return redirect('unauthorized_403')
    return wrapper


def admin_only(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.user_role == 1:
            return view_func(request, *args, **kwargs)
        return redirect('unauthorized_403')
    return wrapper
