from rest_framework import serializers

class OwnedByCompanyModelSerializerMixin(metaclass=serializers.SerializerMetaclass):
    code = serializers.CharField(
        read_only=True, 
        required=False,
    )
    created = serializers.DateTimeField(
        required=False,
        read_only=True, 
        format="%Y-%m-%d %H:%M:%S"
    )
    updated = serializers.DateTimeField(
        required=False,
        read_only=True, 
        format="%Y-%m-%d %H:%M:%S"
    )

    def _set_company(self, instance):
        company = self.context.get('company')
        instance.company = company
        instance.save()

    def create(self, validated_data):
        instance = super().create(validated_data)
        self._set_company(instance=instance)
       
        return instance


class OwnedByCompanyRelatedField(serializers.SlugRelatedField):
    """Queryset removes deleted items and filter by company."""
    
    def __init__(self, slug_field=None, **kwargs):
        super().__init__(slug_field="code", **kwargs)
    
    def get_queryset(self):
        """ Replaces queryset to filter company and deletet_at. """
        queryset = super().get_queryset()
        queryset = queryset.filter(
            company=self.root.context.get("company"),
            deleted_at=None
        )
        return queryset