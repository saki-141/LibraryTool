from django.shortcuts import render
from django.shortcuts import redirect
from .models import Book
from .forms import BookForm
from .forms import FindForm
from django.db.models import Q



def index(request,num=1):
    if (request.method == 'POST'):
        form = FindForm(request.POST)
        str = request.POST['find']
        data = Book.objects.filter(Q(title__contains=str) \
                                   |Q(tag1__contains=str))
    else:
        form = FindForm()
        data = Book.objects.all()
    params={
            'title':'Library',
            'form':form,
            'data':data,
            }
    return render(request, 'Library/index.html',params)


def create(request):
    if (request.method =='POST'):
        obj = Book()
        book = BookForm(request.POST,instance=obj)
        if book.is_valid():
            book.save()
        else:
            print(book.errors)
        return redirect(to='/Library')    
    params ={
            'title':'Add library',
            'form':BookForm(),
            }
    return render(request, 'Library/create.html' ,params)
        
def edit(request,num):
    obj = Book.objects.get(id=num)
    if (request.method== 'POST'):
        book = BookForm(request.POST,instance=obj)
        book.save()
        return redirect(to='/Library')
    params ={
            'title':'Edit data',
            'id':num,
            'form':BookForm(instance=obj),
            }
    return render(request, 'library/edit.html',params)

def delete(request,num):
    book=Book.objects.get(id=num)
    if (request.method == 'POST'):
        book.delete()
        return redirect(to='/Library')
    params = {
            'title':'Delete data',
            'id':num,
            'obj':book,
            }
    return render(request,'library/delete.html',params)

