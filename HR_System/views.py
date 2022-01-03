from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer 


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer): 

    @classmethod 
    def get_token(cls, user):
        token = super().get_token(user)         
        token['role'] = user.role         
        token['username'] = user.username
        token['Personal_Picture'] = str(user.Personal_Picture)
        token['first_name'] = str(user.first_name)
        token['last_name'] = str(user.last_name)
        return token 
        

class CustomTokenObtainPairView(TokenObtainPairView):     
    serializer_class = CustomTokenObtainPairSerializer
