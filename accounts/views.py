import json
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt

from .models import User


@csrf_exempt
def register(request):
    if request.method != "POST":
        return JsonResponse({"error": "Use POST"}, status=405)

    data = json.loads(request.body)
    name = data.get("name", "").strip()
    email = data.get("email", "").strip().lower()
    password = data.get("password", "")
    confirm = data.get("confirm_password", "")

    if not name or not email or not password:
        return JsonResponse({"error": "All fields are required."}, status=400)

    if len(password) < 8:
        return JsonResponse({"error": "Password must be at least 8 characters."}, status=400)

    if password != confirm:
        return JsonResponse({"error": "Passwords do not match."}, status=400)

    if User.objects.filter(email=email).exists():
        return JsonResponse({"error": "This email is already registered."}, status=409)

    user = User.objects.create(
        name=name,
        email=email,
        password_hash=make_password(password),
    )

    return JsonResponse({"message": "Account created!", "user_id": user.user_id}, status=201)
