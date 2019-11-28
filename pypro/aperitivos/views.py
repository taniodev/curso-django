from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao': {'titulo': 'Video Aperitivo: Motivação', 'vimeo_id': 32801864},
        'instalacao-windows': {'titulo': 'Instalação no Windows', 'vimeo_id': 49363935},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
