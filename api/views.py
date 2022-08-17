from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework import status

# Create your views here.

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/inventory/all/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of products with details'
        },
        {
            'Endpoint': 'inventory/id/<int:id>',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product in inventory'
        },
        {
            'Endpoint': 'store/all/',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product in inventory'
        },
    ]
    return Response(routes)

@api_view(['GET'])
def getInventoryProducts(request):
    inventory = InventoryModel.objects.all()
    serializer = InventorySerializer(inventory, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getStoreProducts(request):
    store = StoreModel.objects.all()
    serializer = StoreSerializer(store, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getActions(request):
    action = ActionModel.objects.all()
    serializer = ActionSerializer(action, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def createStoreProduct(request):
    data = request.data
    serializer = StoreSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def createInventoryProduct(request):
    data = request.data
    serializer = InventorySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def createAction(request):
    data = request.data
    print(data)
    serializer = ActionSerializer(data=data)
    try:
        store = StoreModel.objects.get(store_name=data['store_name'], product_name=data['product_name'])
        inventory = InventoryModel.objects.get(product_name=data['product_name'], remained=data['remained'])
        store.del_quantity += int(data['quantity'])
        store.remained += int(data['quantity'])
        store.del_price = data['price']
    except StoreModel.DoesNotExist:
        new_values = {'product_name': data['product_name'], 'del_quantity': data['quantity'], 'del_price': data['price'], 'store_name': data['store_name'], 'deliver': 'Склад', 'del_currency': data['del_currency'], 'remained': data['quantity'], 'percent': 15}
        obj = StoreModel(**new_values)
        obj.save()

    if serializer.is_valid():
        print("Store:", store)
        store.save()
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET', 'PUT', 'DELETE'])
def store_details(request, pk):
    """
    Retrieve, update or delete a store_details.
    """
    try:
        store = StoreModel.objects.get(id=pk)
    except StoreModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StoreSerializer(store, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def inventory_details(request, pk):
    """
    Retrieve, update or delete a inventory_details.
    """
    try:
        inventory = InventoryModel.objects.get(id=pk)
    except InventoryModel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InventorySerializer(inventory, many=False)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InventorySerializer(inventory, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        inventory.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
