from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *

@api_view(['POST'])
def bogie_checksheet_create(request):
    serializer = BogieChecksheetFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": serializer.data
        }, status=201)
    return Response(serializer.errors, status=400)

@api_view(['POST', 'GET'])
def wheel_specifications(request):
    if request.method == 'POST':
        serializer = WheelSpecificationsFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "success": True,
                "message": "Wheel specification submitted successfully.",
                "data": serializer.data
            }, status=201)
        return Response(serializer.errors, status=400)

    if request.method == 'GET':
        filters = {}
        if request.GET.get("formNumber"):
            filters["formNumber"] = request.GET.get("formNumber")
        if request.GET.get("submittedBy"):
            filters["submittedBy"] = request.GET.get("submittedBy")
        if request.GET.get("submittedDate"):
            filters["submittedDate"] = request.GET.get("submittedDate")

        queryset = WheelSpecificationsForm.objects.filter(**filters)
        serializer = WheelSpecificationsFormSerializer(queryset, many=True)

        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        }, status=200)
