from .models import User, UserDetailModel


def get_image_of_user(request):
    context = {"present": False}
    if request.user.is_authenticated:
        usr = User.objects.filter(email=request.user.email).first()
        if usr is not None:
            detail = UserDetailModel.objects.filter(user=usr).first()
            if detail is not None and detail.photo is not None:
                context["present"] = True
                context["loc"] = detail.photo.url
    return context

