def get_user_or_none(request):
    if request.user.is_authenticated():
        return request.user
    return None
