from django.http import Http404
from . models import Album
from django.shortcuts  import render


def index(request):
    all_albums = Album.objects.all()
    context={
        'all_albums':all_albums
    } 
    return render(request,'web2/index.html',context)

def detail(request,album_id):
    #return HttpResponse("<h2> detail for album-id :" + '<br>' + str(album_id)   +"</h2>")
    try:
        album=Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404('album doesnt exist fefe')
    return render(request,'web2/detail.html', {'album':album})