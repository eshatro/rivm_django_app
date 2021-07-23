import pytest

from rivm.rivm.services import CSVService, ServiceError
from rivm.rivm.utils import get_results, transform_to_entry_factory, remove_invalid_rows


def test_csv_service_read():
    csv_service = CSVService(source="rivm/rivm/tests/data/rivm2016.csv")
    result = [row for row in csv_service.read()]
    result_with_headers = (r for r in get_results(result))
    entry_transformed = (e for e in transform_to_entry_factory(result_with_headers))
    clean_data = [row for row in remove_invalid_rows(entry_transformed)]
    first = clean_data[0]
    assert first[0].value == "RIVM_2016"


def test_csv_service_raises_errors():
    csv_service = CSVService()
    # when destination is not provided and write methods are called
    with pytest.raises(ServiceError) as e:
        next(csv_service.read())
    assert e.value.massage == "File name not provided"
