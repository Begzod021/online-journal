from rest_framework import serializers
from users.models import User, Teacher, Pupil
from rest_framework_simplejwt.tokens  import RefreshToken
from information.models import Journal
from information.api.serializers import JournalSerializer, ClassNumSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only = True, required = True, style = {"input_type":"password"}
    )



    class Meta:
        model = User

        exclude = ['approve', 'is_superuser', "is_active", "groups", "user_permissions", "last_login", "date_joined", "email"]



    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password":"Password fields didn't match."})

        return attrs



    def create(self, validated_data):

        if validated_data["role"] == "admin":
            validated_data["is_staff"] = True
            user = User.objects.create(
                username = validated_data["username"],
                first_name = validated_data["first_name"],
                last_name = validated_data["last_name"],
                role = validated_data["role"],
                is_staff = validated_data["is_staff"],
            )
            user.set_password(validated_data["password"])
            user.save()

            return user
        
        elif validated_data["role"] == "teacher":
            validated_data["is_staff"] = False
            user = Teacher.objects.create(
                username = validated_data["username"],
                first_name = validated_data["first_name"],
                last_name = validated_data["last_name"],
                role = validated_data["role"],
                is_staff = validated_data["is_staff"],
                approve = True
            )
            user.set_password(validated_data["password"])
            user.save()

            return user

        elif validated_data["role"] == "pupil":
            validated_data["is_staff"] = False
            user = Pupil.objects.create(
                username = validated_data["username"],
                first_name = validated_data["first_name"],
                last_name = validated_data["last_name"],
                role = validated_data["role"],
                is_staff = validated_data["is_staff"],
                class_number = validated_data["class_number"]
            )
            user.set_password(validated_data["password"])
            user.save()

            return user





class UserSerializer(serializers.ModelSerializer):
    class_number = serializers.SerializerMethodField(
        read_only = True
    )
    class Meta:
        model = User
        fields = ["id","username", "email", "first_name", "last_name", "role", "last_login", "class_number"]

    def get_class_number(self, obj):
        class_number = obj.class_number
        serializer_class = ClassNumSerializer(class_number, many = False)

        return serializer_class.data



class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField(read_only = True)
    class_number = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ["username", "id", "first_name", "role", "approve", "token", "class_number"]

    def get_token(self, obj):

        token = RefreshToken.for_user(obj)
        return str(token.access_token)

    def get_class_number(self, obj):

        class_num = obj.class_number
        serializer = ClassNumSerializer(class_num, many=False)

        return serializer.data

class PupilSerializer(serializers.ModelSerializer):
    class_number = serializers.SerializerMethodField(
        read_only = True
    )
    class Meta:
        model = Pupil
        fields = ["id","username", "email", "first_name", "last_name", "role", "class_number", "last_login"]

    def get_class_number(self, obj):
        class_number = obj.class_number

        serializer_class = ClassNumSerializer(class_number, many = False)

        return serializer_class.data

class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ["id", "username", "email", "first_name", "last_name","role", "approve", "last_login"]


class TeacherProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ["username", "email", "first_name", "last_name", "role", "id"]


class PupilProfileSerializer(serializers.ModelSerializer):
    class_number = serializers.SerializerMethodField(
        read_only = True
    )
    class Meta:
        model = Pupil
        fields = ["username", "email", "first_name", "last_name", "class_number", "role"]

    def get_class_number(self, obj):
        class_number = obj.class_number

        serializer_class = ClassNumSerializer(class_number, many=False)

        return serializer_class.data