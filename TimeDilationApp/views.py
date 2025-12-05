from django.http import JsonResponse
from django.shortcuts import render
import math

# Constants
C = 299792458  # speed of light (m/s)


# Render the HTML page
def time_visualizer(request):
    return render(request, "time.html")


# API: Time Dilation Calculation
def calculate_dilation(request):
    # Read velocity from query params
    velocity = request.GET.get("velocity", "0").replace(" ", "")

    # Safe parsing
    try:
        velocity = float(velocity)
    except ValueError:
        velocity = 0

    # Clamp velocity to below 1c
    if velocity >= 1:
        velocity = 0.999999999

    # γ = 1 / sqrt(1 - v²)
    gamma = 1 / math.sqrt(1 - velocity**2)

    return JsonResponse({"dilation_factor": gamma})
