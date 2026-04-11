from decimal import Decimal

from rest_framework import serializers

from .models import Operator, Transaction, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'name', 'card_number', 'created_at')


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = ('id', 'username', 'name', 'created_at')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = (
            'id',
            'user',
            'type',
            'amount',
            'recharge_method',
            'operator',
            'created_at',
        )


class OnlineRechargeSerializer(serializers.Serializer):
    card_number = serializers.CharField(max_length=50)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=Decimal('0.01'))


class OperatorRechargeSerializer(serializers.Serializer):
    card_number = serializers.CharField(max_length=50)
    operator_id = serializers.UUIDField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2, min_value=Decimal('0.01'))
    recharge_method = serializers.ChoiceField(choices=Transaction.MethodType.choices)

    def validate_recharge_method(self, value):
        if value == Transaction.MethodType.ONLINE:
            raise serializers.ValidationError('Use CASH or CARD for in-person recharge.')
        return value


class TurnstileValidationSerializer(serializers.Serializer):
    card_number = serializers.CharField(max_length=50)
    meal_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        min_value=Decimal('0.01'),
        required=False,
        default=Decimal('5.00'),
    )


class BalanceResponseSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)


class AccessResponseSerializer(serializers.Serializer):
    access_granted = serializers.BooleanField()
    message = serializers.CharField()
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)


class CardLookupResponseSerializer(serializers.Serializer):
    user = UserSerializer()
    balance = serializers.DecimalField(max_digits=10, decimal_places=2)
    photo_available = serializers.BooleanField()

