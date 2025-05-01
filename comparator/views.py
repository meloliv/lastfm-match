from django.shortcuts import render
from .utils import get_top_artists

def index(request):
    if request.method == 'POST':
        user1 = request.POST['user1']
        user2 = request.POST['user2']

        artists1 = get_top_artists(user1)
        artists2 = get_top_artists(user2)

        common_artists = list(set(artists1) & set(artists2))

        return render(request, 'comparator/index.html', {
            'user1': user1,
            'user2': user2,
            'common_artists': common_artists,
        })

    return render(request, 'comparator/index.html')
