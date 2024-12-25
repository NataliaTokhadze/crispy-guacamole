from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Video
from django.urls import reverse

def index(request):
    return render(request, 'meow/index.html')

class CreateVideo(CreateView):
    model = Video
    fields = ['title', 'description', 'video_file', 'thumbnail']
    template_name = 'meow/create_video.html'

    # def get_success_url(self):
    #     return reverse('video-detail', kwargs={'pk': self.object.pk})