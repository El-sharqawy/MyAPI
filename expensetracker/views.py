from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Sum
from .models import IncomeSource, Expense, Transaction
from users.models import CustomUser
from .serializers import UserSerializer, IncomeSourceSerializer, ExpenseSerializer, TransactionSerializer

class UserCreateView(generics.CreateAPIView):

class UserDetailView(generics.RetrieveUpdateAPIView):

class UserBalanceView(APIView):


class IncomeSourceListCreateView(generics.ListCreateAPIView):

class IncomeSourceDetailView(generics.RetrieveUpdateDestroyAPIView):

class ExpenseListCreateView(generics.ListCreateAPIView):

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):

class TransactionListCreateView(generics.ListCreateAPIView):

class TransactionDetailView(generics.RetrieveUpdateDestroyAPIView):

class TransactionSummaryView(APIView):
