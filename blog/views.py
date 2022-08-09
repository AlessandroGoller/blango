from django.shortcuts import render
from .models import posts

# Create your views here.
import logging
logger = logging.getLogger(__name__)


logger.debug("Got %d posts", len(posts))
