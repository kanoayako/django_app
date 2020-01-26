from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Friend
from .forms import FriendForm
from .forms import FindForm
# from .forms import HelloForm
# from django.db.models import QuerySet

def index(request):
    data = Friend.objects.all()
    params = {
        'title': 'Helllo',
        'data': data,
    }
    return render(request, 'hello/index.html', params)
#create model
def create(request):
    if (request.method == 'POST'):
        obj = Friend()
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'form': FriendForm(),
    }
    return render(request, 'hello/create.html', params)
def edit(request, num):
    obj = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend = FriendForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id':num,
        'form': FriendForm(instance=obj),
    }
    return render(request, 'hello/edit.html', params)
def delete(request, num):
    friend = Friend.objects.get(id=num)
    if (request.method == 'POST'):
        friend.delete()
        return redirect(to='/hello')
    params = {
        'title': 'Hello',
        'id':num,
        'obj': friend,
    }
    return render(request, 'hello/delete.html', params)
def find(request):
    if (request.method == 'POST'):
        msg = 'search result:'
        form = FindForm(request.POST)
        str = request.POST['find']
        list = str.split()
        data = Friend.objects.filter(name__in=list)
    else:
        msg = 'search words...'
        form = FindForm()
        data = Friend.objects.all()
    params = {
        'title': 'Hello',
        'message': msg,
        'form':form,
        'data':data,        
    }
    return render(request, 'hello/find.html', params)

    # params = {
    #     'title': 'Helllo',
    #     'form': HelloForm(),
    # }
    # if (request.method == 'POST'):
    #     name = request.POST['name']
    #     mailadd = request.POST['mailadd']
    #     birthday = request.POST['birthday']
    #     size = int(request.POST['size'])
    #     heel = int(request.POST['heel'])
    #     fvbr = request.POST['fvbr']
    #     fvshbr = request.POST['fvshbr']
    #     fvclbr = request.POST['fvclbr']
    #     zodata = request.POST['zodata'] 
    #     appdata = request.POST['appdata']
    #     add = request.POST['add']
    #     ofadd = request.POST['ofadd']
    #     ofty = request.POST['ofty']
    #     posi = request.POST['post']
    #     out = request.POST['out']
    #     pur = request.POST['pur']
    #     situ = request.POST['situ']
    #     friend = Friend(name=name,mailadd=mailadd,birthday=birthday,size=size,heel=heel,fvbr=fvbr,fvshbr=fvshbr,fvclbr=fvclbr,zodata=zodata,appdata=appdata,add=add,ofadd=ofadd,ofty=ofty,posi=posi,out=out,pur=pur,situ=situ)
    #     friend.save()
    #     return redirect(to='/hello')
    # return render(request, 'hello/create.html', params)        

# from .forms import HelloForm
# from django.views.generic import TemplateView
# from .forms import HelloForm

# def __new_str__(self):
#     result = ''
#     for item in self:
#         result += '<tr>'
#         for k in item:
#             result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
#         result += '</tr>'
#     return result

# QuerySet.__str__ = __new_str__

# def index(request):
#     data = Friend.objects.all().values('id', 'name', 'size')
#     params = {
#         'title': 'Helllo',
#         'data': data,
#     }

# def index(request):
#     num = Friend.objects.all().count()
#     first = Friend.objects.all().first()
#     last = Friend.objects.all().last()
#     data = [num, first, last]
    # data = Friend.objects.all().values_list("id", "name", "size")
    
# def index(request):
#     params = {
#         'title': 'Helllo',
#         'message': 'all friends.',
#         'form': HelloForm(),
#         'data': [],
#     }
#     if (request.method == 'POST'):
#         num=request.POST["id"]
#         item = Friend.objects.get(id=num)
#         params["data"] = [item]
#         params["form"] = HelloForm(request.POST)
#     else:
#         params["data"] = Friend.objects.all()
    

# class HelloView(TemplateView):

#     def __init__(self):
#         self.params = {
#                 'title': 'Helllo',
#                 # 'message': 'your data:',
#                 'form': HelloForm(),
#                 'result': None
#             }

#     def get(self, request):
#         return render(request, 'hello/index.html', self.params)

#     def post(self, request):
#         ch = request.POST.getlist('choice')
#         result = '<ol><b>selected:</b>'
#         for item in ch:
#             result += '<li>' + item + '</li>'
#         result += '</ol>'
#         self.params['result'] = result
#         self.params['form'] = HelloForm(request.POST)
#         return render(request, 'hello/index.html', self.params)

        # msg = 'あなたは、<b>' +request.POST['name'] + \
        #     ' (' +request.POST['age'] + \
        #     ') </b>さんです。<br>メールアドレスは、<b>' +request.POST['mail'] + \
        #     '</b>さんですね。'
        # self.params['message'] = msg

# def index(request):
#     params = {
#             'title': 'Helllo',
#             'message': 'your data:',
#             'form': HelloForm()
#     }
#     if (request.method == 'POST'):
#         params['message'] = '名前: ' + request.POST['name'] + \
#            '<br>メール: ' + request.POST['mail'] + \
#            '<br>年齢: ' + request.POST['age']
#         params['form'] = HelloForm(request.POST)
#     return render(request, 'hello/index.html', params)


# Create your views here.
 