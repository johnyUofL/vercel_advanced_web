import json
from django.test import TestCase
from django.urls import reverse
from django.urls import reverse_lazy
# importing as in the video tutorial
from rest_framework import APIRequestFactory
from rest_framework.test import APITestCase
# importing models and serializers as in the tutorial
from .model_factories import *
from .serializers import *
