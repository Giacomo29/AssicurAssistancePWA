from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import (CreateCustomUserSerializer,
                                    LoginCustomUserSerializer,
                                    CustomUserSerializer, 
                                    UserDisplaySerializer,
                                    ResetPasswordEmailRequestSerializer,
                                    SetNewPasswordSerializer,UpdateCustomUserSerializer,AvatarSerializer,ChangePasswordSerializer
                                    )
from rest_framework import generics, status
from users.models import CustomUser, Notification
from rest_framework.permissions import IsAuthenticated
from .permission import IsServer

from rest_framework_simplejwt.tokens import RefreshToken
from users.utils import Util
from django.contrib.sites.shortcuts import get_current_site 
from django.urls import reverse
import jwt
from django.conf import settings
from django.contrib.auth.tokens  import PasswordResetTokenGenerator
from django.utils.encoding import smart_str,force_str ,smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site 
from django.urls import reverse
from users.utils import Util
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.generics import GenericAPIView

from rest_framework.authentication import get_authorization_header
from rest_framework.exceptions import AuthenticationFailed



# Mostra l'utente corrente
class CurrentUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = CustomUserSerializer(request.user)
        user = request.user
        return Response(CustomUserSerializer(user, context={'request': request}).data)
        



# classe per la registrazione dell'utente con email verification 
class CustomUserAPIView(APIView):

    def get(self,request):
        #serializer = CustomUserSerializer(request.user, context={'request': request})
        serializer = CustomUserSerializer(request.user)
        return Response(serializer.data)



class ChangeAvatarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, format=None):
        user = request.user
        serializer = AvatarSerializer(instance=user, data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class UserDetailView(RetrieveUpdateAPIView):
    serializer_class = UpdateCustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Restituisci l'oggetto utente corrente
        return self.request.user
    
    
class UserProfileImageView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterAPIView(generics.GenericAPIView):
    serializer_class  = CreateCustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        #email verification
        user_data = serializer.data
        user = CustomUser.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user)

        current_site = '127.0.0.1:8000'
        #get_current_site(request).domain
        relativeLink = reverse('email-verify')
        
        absurl = 'http://'+current_site+relativeLink+"?token="+str(token)
        email_body = 'Ciao '+user.username+' clicca sul link per verificare il tuo account\n'+absurl
        data={'email_body': email_body,'to_email': user.email ,'email_subject': 'Verify your email', 'to': user.email}

        Util.send_email(data)


        response_data = {
            'user': CustomUserSerializer(user, context=self.get_serializer_context()).data,
            'access': str(token.access_token),
            'refresh': str(token)
        }


        return Response(response_data, status=status.HTTP_201_CREATED)
        
        
        
        





# classe per la verifica dell'email tramite registrazione rest api
class VerifyEmail(generics.GenericAPIView):
    def get(self,request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            user = CustomUser.objects.get(id=payload['user_id'])

            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

    

    

# classe per il login dell'utente tramite rest
class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginCustomUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        
        
        refresh = RefreshToken.for_user(user)
        response = Response()

        response.data = {
            'user' : CustomUserSerializer(user, context=self.get_serializer_context()).data,
            'access': str(refresh.access_token),
            'refresh': str(refresh)
        }
        
        return response
    
    
class RefreshAPIView(APIView):
    def post(self,request):
        refresh_token = request.COOKIES.get('refreshToken')
        id = decode_refresh_token(refresh_token)
        access_token = create_access_token(id)
        
        return Response({'token': access_token})
    
    
# class LogoutAPIView(APIView):  
#     authentication_classes = []
#     def post(self,_):
#         response = Response()
#         response.delete_cookie('refreshToken')
#         response.data = {
#             'message': 'success'
#         }
#         return response



class LogoutAPIView(APIView):
    def post(self, request,format=None):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({'message': 'Logout success'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Logout failed'}, status=status.HTTP_400_BAD_REQUEST)



class AddNotification(APIView):
    permission_classes = [IsServer]

    def post(self, request):
        server = CustomUser.objects.get(username="server")
        notification_text = request.data.get('notification') 

        if notification_text:
            notification = Notification.objects.create(user=server, notification=notification_text)
            return Response({'message': 'Notification added'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Notification text is required'}, status=status.HTTP_400_BAD_REQUEST)
        

class RequestPasswordResetEmail(generics.GenericAPIView):
    
    serializer_class = ResetPasswordEmailRequestSerializer

    def post(self, request):

        try:
            serializer = self.serializer_class(data=request.data)
            
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            email = serializer.validated_data['email']

            if not CustomUser.objects.filter(email=email).exists():
                return Response({'email': 'No user with this email'}, status=status.HTTP_400_BAD_REQUEST)

            user = CustomUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            #current_site = get_current_site(request=request).domain
            # current_site = '127.0.0.1:8000'
            # relative_link = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            # absurl = 'http://' + current_site + relative_link
            
            
            current_site = '127.0.0.1:8080'
            #relative_link = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://' + current_site + "/password-reset/?uidb64=" + uidb64 + "&token=" + token
            
            email_body = 'Ciao,\n Clicca il link in basso per il reset della tua password\n' + absurl
            data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Reset your password', 'to': user.email}

            Util.send_email(data)

            return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PasswordTokenCheckAPI(generics.GenericAPIView):
    def get(self,request,uidb64,token):
        
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = CustomUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user,token):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)
            
            return Response({'success': True, 'message': 'Credentials Valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            #if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)



class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class  = SetNewPasswordSerializer

    def patch(self,request):
        serializer=self.serializer_class(data = request.data)
        

        serializer.is_valid(raise_exception=True)
        return Response({'success':'True','message':'Password reset success'},status=status.HTTP_200_OK)
    


class ChangePasswordView(generics.UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer