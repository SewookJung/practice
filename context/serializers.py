from rest_framework.serializers import Serializer, ModelSerializer, SerializerMethodField

from .models import Context


class ProvideContextSerializer(ModelSerializer):
    """ContextSerializer _summary_

    _extended_summary_

    Args:
        ModelSerializer (_type_): _description_
    """

    
    def get_field_names(self, declared_fields, info):
        context = self.context
        print(context) # {"request": value ,"view": value, "format": value}

        
        if self.context:
            request = self.context.get("request", None)
            
            if request and hasattr(request, "user"):
                user = request.user
                print(user)

        return super().get_field_names(declared_fields, info)
    

    class Meta:
        model = Context
        fields = "__all__"
    

    
class NotProvideContextSerializer(ModelSerializer):

    def get_field_names(self, declared_fields, info):
        context = self.context
        print(context) # {}
        return super().get_field_names(declared_fields, info)
    

    class Meta:
        model = Context
        fields = "__all__"


class CustomContextSerializer(ModelSerializer):

    def get_field_names(self, declared_fields, info):
        context = self.context
        print(context)
        return super().get_field_names(declared_fields, info)
    
    class Meta:
        model = Context
        fields = "__all__"