from decimal import Decimal

from django.db import transaction
from django.db.models import Case, DecimalField, F, Sum, Value, When
from django.db.models.functions import Coalesce
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Operator, Transaction, User
from .serializers import (
    CardLookupResponseSerializer,
    OnlineRechargeSerializer,
    OperatorRechargeSerializer,
    TransactionSerializer,
    TurnstileValidationSerializer,
    UserSerializer,
)


def calculate_user_balance(user: User) -> Decimal:
    signed_amount = Case(
        When(type=Transaction.TransactionType.RECHARGE, then=F('amount')),
        When(type=Transaction.TransactionType.MEAL, then=-F('amount')),
        default=Value(Decimal('0.00')),
        output_field=DecimalField(max_digits=10, decimal_places=2),
    )
    result = user.transactions.aggregate(
        balance=Coalesce(
            Sum(signed_amount),
            Value(Decimal('0.00')),
            output_field=DecimalField(max_digits=10, decimal_places=2),
        )
    )
    return result['balance']


class OnlineRechargeView(APIView):
    def post(self, request):
        serializer = OnlineRechargeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User, card_number=serializer.validated_data['card_number'])
        recharge = Transaction.objects.create(
            user=user,
            type=Transaction.TransactionType.RECHARGE,
            amount=serializer.validated_data['amount'],
            recharge_method=Transaction.MethodType.ONLINE,
        )

        return Response(
            {
                'transaction': TransactionSerializer(recharge).data,
                'balance': calculate_user_balance(user),
            },
            status=status.HTTP_201_CREATED,
        )


class OperatorRechargeView(APIView):
    def post(self, request):
        serializer = OperatorRechargeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User, card_number=serializer.validated_data['card_number'])
        operator = get_object_or_404(Operator, id=serializer.validated_data['operator_id'])

        recharge = Transaction.objects.create(
            user=user,
            type=Transaction.TransactionType.RECHARGE,
            amount=serializer.validated_data['amount'],
            recharge_method=serializer.validated_data['recharge_method'],
            operator=operator,
        )

        return Response(
            {
                'transaction': TransactionSerializer(recharge).data,
                'balance': calculate_user_balance(user),
            },
            status=status.HTTP_201_CREATED,
        )


class UserBalanceView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        return Response({'user_id': user.id, 'balance': calculate_user_balance(user)})


class UserTransactionHistoryView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        queryset = user.transactions.order_by('-created_at')
        tx_type = request.query_params.get('type')

        if tx_type:
            queryset = queryset.filter(type=tx_type)

        return Response(TransactionSerializer(queryset, many=True).data)


class TurnstileValidationView(APIView):
    @transaction.atomic
    def post(self, request):
        serializer = TurnstileValidationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = get_object_or_404(User, card_number=serializer.validated_data['card_number'])
        meal_price = serializer.validated_data['meal_price']
        balance = calculate_user_balance(user)

        if balance < meal_price:
            return Response(
                {
                    'access_granted': False,
                    'message': 'Insufficient balance.',
                    'balance': balance,
                },
                status=status.HTTP_200_OK,
            )

        Transaction.objects.create(
            user=user,
            type=Transaction.TransactionType.MEAL,
            amount=meal_price,
        )
        new_balance = calculate_user_balance(user)

        return Response(
            {
                'access_granted': True,
                'message': 'Access granted.',
                'balance': new_balance,
            },
            status=status.HTTP_200_OK,
        )


class CardLookupView(APIView):
    def get(self, request, card_number):
        user = get_object_or_404(User, card_number=card_number)
        payload = {
            'user': UserSerializer(user).data,
            'balance': calculate_user_balance(user),
            'photo_available': False,
        }
        return Response(CardLookupResponseSerializer(payload).data)
