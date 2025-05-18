from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

@api_view(['POST'])
def wagmi_view(request):
    data = request.data

    # Ping response (empty body)
    if not data:
        return Response({
            "message": "wagmi",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "lang": "Python",
        })

    a = data.get("a")
    b = data.get("b")

    # Validation
    if a is None or b is None:
        return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

    if a < 0 or b < 0:
        return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

    if a + b > 100:
        return Response({"error": "Invalid input"}, status=status.HTTP_400_BAD_REQUEST)

    return Response({
        "result": a + b,
        "a": a,
        "b": b,
        "status": "success"
    })
