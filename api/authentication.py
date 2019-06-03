from rest_framework.authentication import TokenAuthentication
from .models import User

class MyTokenAuthentication(TokenAuthentication):
    model = User