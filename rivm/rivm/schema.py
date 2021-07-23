import graphene
from graphene_django import DjangoObjectType
from rivm.rivm.models import Impact, Indicator, Entry, Geography


class IndicatorType(DjangoObjectType):
    class Meta:
        model = Indicator
        fields = ('id', 'method', 'category', 'indicator', 'unit')


class ImpactType(DjangoObjectType):
    class Meta:
        model = Impact
        fields = (
            'id',
            'indicator',
            'entry',
            'coefficient',
        )


class EntryType(DjangoObjectType):
    impact = graphene.Field(ImpactType, id=graphene.Int())

    class Meta:
        model = Entry
        fields = (
            'id',
            'product_name',
            'geography',
            'unit',
        )


class GeographyType(DjangoObjectType):
    class Meta:
        model = Geography
        fields = ('short_name', 'name')


class Query(graphene.ObjectType):
    indicator = graphene.Field(IndicatorType, id=graphene.Int())
    indicators = graphene.List(IndicatorType)

    entry = graphene.Field(EntryType, id=graphene.Int())
    entries = graphene.List(EntryType)

    impact = graphene.Field(ImpactType, id=graphene.Int(), indicator_id=graphene.Int())

    def resolve_indicator(root, info, id):
        # Querying a list
        return Indicator.objects.get(pk=id)

    def resolve_indicators(root, info, **kwargs):
        # Querying a list
        return Indicator.objects.all()

    def resolve_entry(root, info, id):
        # Querying a list
        return Entry.objects.get(pk=id)

    def resolve_entries(root, info, **kwargs):
        # Querying a list
        return Entry.objects.all()

    def resolve_impact(root, info, id, indicator_id):
        # Querying a list
        return Impact.objects.get(pk=id, indicator_pk=indicator_id)


schema = graphene.Schema(query=Query)
