from rest_framework import serializers
from users.models import CustomUser
from .models import IncomeSource, Expense, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'current_balance']

class IncomeSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeSource
        fields = ['id', 'name', 'description']

class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ['id', 'name', 'category']

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'income_source', 'expense', 'amount', 'transaction_date', 'description', 'type']
