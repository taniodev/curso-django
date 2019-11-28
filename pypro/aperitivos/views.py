from django.shortcuts import render


def video(request, slug):
    video = {
        'titulo': 'Video Aperitivo: Motivação',
        'vimeo_id': 32801864,
    }
    return render(request, 'aperitivos/video.html', context={'video': video})
