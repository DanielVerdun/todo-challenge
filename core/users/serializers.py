
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

"""
    UserSerializer es la class que se encargará de serializar nuestro moldels User
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['email','password', 'name']
        extra_kwargs ={'password':{'write_only':True}}

    def create(self, validate_data):
        return get_user_model().objects.create_user(**validate_data)

    def update(self, instance, validate_data ):
        password = validate_data.pop('password', None)
        user = super().update(instance, validate_data )

        if password:
            user.set_password(password)
            user.save()

        return user


class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'})

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )

        if not user:
            raise serializers.ValidationError('No se pudo autenticat', code='authorization')

        data['user'] = user
        return data