from rivm.rivm.models import Indicator, Impact
from rivm.rivm.utils import indicator_only


def impact_factory(row, entry):
    for i, indicator in enumerate(row):
        if i < 3 or indicator.value == "" or not indicator.value:
            continue
        header, cat, indi = indicator.header.split(":")
        ind = Indicator.objects.filter(method=header, category=cat, indicator=indi).first()
        # ASSUMPTION: that an indicator value is actually the coefficient of the impact
        im = Impact(indicator=ind, entry=entry, coefficient=indicator.value)
        yield im


def indicator_factory(first):
    for i in list(filter(indicator_only, first)):
        method, category, indicator = i.header.split(":")
        yield Indicator(method=method[:45], category=category[:45], indicator=indicator[:45], unit=i.unit)
