from django.shortcuts import redirect , reverse
from django.http import JsonResponse


def login_decorators(func):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated():
            return func(request,*args,**kwargs)
        else:
            #如果是ajax请求 
            if request.is_ajax():
                return JsonResponse({'status':'nologin'})

            url = request.get_full_path()
            ret = redirect(reverse('users:login'))
            ret.set_cookie('url',url)
            return ret
    return inner


