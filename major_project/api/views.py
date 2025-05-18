# api/ml_utils/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET
from django.contrib.auth.models import User
from .models import GlucoseReading
from .ml_utils.ml_model import predict_glucose
import json

@csrf_exempt
def predict_glucose_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            features = data.get('features')

            if not user_id or not features or not isinstance(features, list):
                return JsonResponse({'error': 'Invalid input. "features" must be a list.'}, status=400)

            if len(features) != 50:
                return JsonResponse({'error': 'Expected 50 averaged sensor values in "features".'}, status=400)

            # Predict glucose level
            glucose_level = predict_glucose(features)

            # Save to database
            user = User.objects.get(id=user_id)
            reading = GlucoseReading.objects.create(
                user=user,
                raw_data={'features': features},
                glucose_level=glucose_level
            )

            return JsonResponse({
                'glucose_level': glucose_level,
                'timestamp': reading.timestamp
            }, status=200)

        except User.DoesNotExist:
            return JsonResponse({'error': 'User does not exist.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST method is allowed.'}, status=405)


def list_glucose_readings_view(request):
    if request.method == 'GET':
        try:
            user_id = request.GET.get('user_id')

            if not user_id:
                return JsonResponse({'error': 'User ID is required.'}, status=400)

            readings = GlucoseReading.objects.filter(user_id=user_id).order_by('-timestamp')
            results = [
                {
                    'id': reading.id,
                    'raw_data': reading.raw_data,
                    'glucose_level': reading.glucose_level,
                    'timestamp': reading.timestamp
                }
                for reading in readings
            ]

            return JsonResponse({'readings': results}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only GET method is allowed.'}, status=405)

@require_GET
def glucose_levels_only_view(request):
    try:
        user_id = request.GET.get('user_id')

        if not user_id:
            return JsonResponse({'error': 'User ID is required.'}, status=400)

        readings = GlucoseReading.objects.filter(user_id=user_id).order_by('-timestamp')
        results = [
            {
                'glucose_level': reading.glucose_level,
                'timestamp': reading.timestamp
            }
            for reading in readings
        ]

        return JsonResponse({'glucose_levels': results}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
