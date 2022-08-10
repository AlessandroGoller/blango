from django.shortcuts import render
from .models import posts
#from django.views.decorators.cache import cache_page

# Create your views here.
import logging
logger = logging.getLogger(__name__)

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    logger.debug("Got %d posts", len(posts))
    return render(request, "blog/index.html", {"posts": posts})

logger.debug("Got %d posts", len(posts))
