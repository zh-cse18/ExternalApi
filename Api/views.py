from rest_framework import generics

from ApiUse.models import Quote, QuoteCategory
from .serializers import QuoteSerializer, QuoteCategorySerializer


class QuoteApiView(generics.ListAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteCategoryApiView(generics.ListAPIView):
    queryset = QuoteCategory.objects.all()
    serializer_class = QuoteCategorySerializer


class QuoteApiDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer


class QuoteApiNewView(generics.ListCreateAPIView):
    queryset = Quote.objects.all().order_by('-id')[:1]
    serializer_class = QuoteSerializer
