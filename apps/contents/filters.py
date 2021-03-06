from django_filters.rest_framework import (
    filters,
    filterset,
)

from ..filters import (
    UUIDListFilter,
)
from .models import (
    Content,
)


class ContentFilterSet(filterset.FilterSet):
    label__contains = filters.CharFilter(
        field_name='label',
        lookup_expr='contains',
    )
    uuid__in = UUIDListFilter(
        field_name='uuid',
        lookup_expr='in',
    )

    class Meta:
        model = Content
        fields = [
            'uuid',
            'uuid__in',
            'label',
            'label__contains',
            'created_user',
        ]
