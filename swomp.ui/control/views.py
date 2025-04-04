from django.shortcuts import render
from django.http import JsonResponse
import serial

# Try to establish a UART connection with SHREC
try:
    ser = serial.Serial('/dev/ttyS0', 9600, timeout=1)
    ser.flush()
except Exception as e:
    print(f"UART Connection Error: {e}")

def control_panel(request):
    return render(request, 'control/index.html')

def control_device(request, device_name, action):
    try:
        command = f"{device_name}:{action}\n"
        ser.write(command.encode('utf-8'))  # Send command to SHREC
        return JsonResponse({"message": f"{device_name} turned {action}"})  # ✅ Fixed indentation
    except Exception as e:
        return JsonResponse({"error": f"Failed to send command: {e}"})

