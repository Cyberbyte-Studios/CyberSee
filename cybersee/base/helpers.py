def get_user_or_none(request):
    if request and request.user and request.user.is_authenticated():
        return request.user
    return None
