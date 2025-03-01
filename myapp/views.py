from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import UserData

@csrf_exempt  # Disables CSRF for testing; use proper CSRF handling in production
def receive_data(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Get JSON data from request body
            name = data.get("name", "Unknown")  # Extract "name" from request
            print("Received name:", name)

            # Save data to the database
            user = UserData.objects.create(name=name)
            user.save()

            response_data = {
                "message": f"Received name: {name}",
                "status": "Success"
            }
            return JsonResponse(response_data, status=200)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

    return JsonResponse({"error": "Only POST requests allowed"}, status=405)
