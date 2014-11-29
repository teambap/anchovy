from users.models import Profile


def save_profile(backend, details, response, user, is_new=False, *args, **kwargs):
    if backend.name == 'twitter':
        user_profile = None
        if is_new:
            user_profile = Profile.objects.get_or_create(user=user)[0]
        else:
            user_profile = Profile.objects.get(user=user)

        profile_image_url = response.get('profile_image_url')
        print('profile_image_url : %s' % (profile_image_url))
        user_profile.profile_image_url = profile_image_url
        user_profile.save()