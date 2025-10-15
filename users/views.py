from django.contrib.auth import get_user_model, authenticate, login as auth_login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile
import requests
import os

User = get_user_model()

# -------- Signup API --------
@csrf_exempt
@api_view(['POST'])
def signup_api(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')
    full_name = data.get('full_name')
    role = data.get('role')

    if not all([email, password, full_name, role]):
        return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=email).exists():
        return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create(username=email, email=email, full_name=full_name, role=role)
        user.set_password(password)
        user.save()

        # Create user profile
        UserProfile.objects.create(user=user, email=email, full_name=full_name, role=role)

        # Set backend explicitly
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth_login(request, user)

        return Response({"message": "User created successfully", "username": user.username}, status=status.HTTP_201_CREATED)
    except Exception as e:
        print("Signup error:", e)
        return Response({"error": "Internal Server Error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# -------- Login API --------
@csrf_exempt
@api_view(['POST'])
def login_api(request):
    data = request.data
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return Response({"error": "Email and password are required"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(request, username=email, password=password)
    if user:
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth_login(request, user)
        return Response({"message": "Login successful"}, status=status.HTTP_200_OK)

    return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


# -------- GitHub OAuth Login (only on login page) --------
@csrf_exempt
@api_view(['POST'])
def github_login(request):
    code = request.data.get('code')
    if not code:
        return Response({"error": "No code provided"}, status=status.HTTP_400_BAD_REQUEST)

    client_id = os.getenv("GITHUB_CLIENT_ID")
    client_secret = os.getenv("GITHUB_CLIENT_SECRET")

    # Exchange code for access token
    token_res = requests.post(
        'https://github.com/login/oauth/access_token',
        headers={'Accept': 'application/json'},
        data={
            'client_id': client_id,
            'client_secret': client_secret,
            'code': code
        }
    )

    token_data = token_res.json()
    access_token = token_data.get('access_token')
    if not access_token:
        return Response({"error": "Failed to get access token"}, status=status.HTTP_400_BAD_REQUEST)

    # Get GitHub user info
    user_res = requests.get(
        'https://api.github.com/user',
        headers={'Authorization': f'token {access_token}'}
    )
    user_data = user_res.json()
    email = user_data.get('email') or f"{user_data['login']}@github.com"
    full_name = user_data.get('name') or user_data['login']

    # Check if user exists, else create
    user, created = User.objects.get_or_create(
        username=email,
        defaults={'email': email, 'full_name': full_name, 'role': 'developer'}
    )

    if created:
        UserProfile.objects.create(user=user, email=email, full_name=full_name, role='developer')

    # Set backend explicitly
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    auth_login(request, user)

    return Response({"message": "GitHub login successful"}, status=status.HTTP_200_OK)


# -------- Dashboard API --------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def dashboard(request):
    user = request.user
    return Response({
        "message": f"Welcome {user.full_name}",
        "email": user.email,
        "role": user.role
    })


# -------- Auth Check API --------
@api_view(['GET'])
def check_auth(request):
    if request.user.is_authenticated:
        return Response({
            "is_authenticated": True,
            "full_name": request.user.full_name,
            "email": request.user.email,
            "role": request.user.role
        })
    return Response({"is_authenticated": False}, status=status.HTTP_401_UNAUTHORIZED)


















