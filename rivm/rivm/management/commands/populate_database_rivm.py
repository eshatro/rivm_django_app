import sys

from tqdm import tqdm
from django.core.management.base import BaseCommand
from rivm.rivm.models import Indicator, Entry, DataSource, Impact, Geography
from rivm.rivm.services import CSVService
from rivm.rivm.utils import get_results, transform_to_entry_factory, remove_invalid_rows
from rivm.rivm.factories import impact_factory, indicator_factory


class Command(BaseCommand):
    help = 'Populates the database from a csv file'

    def add_arguments(self, parser):
        parser.add_argument('file_location', type=str)

    def handle(self, *args, **options):
        file_name = options["file_location"]
        csv_service = CSVService(source=file_name)

        # prepare rows
        result = [row for row in csv_service.read()]
        result_with_headers = (r for r in get_results(result))
        entry_transformed = (e for e in transform_to_entry_factory(result_with_headers))
        clean_data = [row for row in remove_invalid_rows(entry_transformed)]

        first = clean_data[0]
        data_store = first[0].value
        # populate data source from the file all data is being loaded
        # insert first data store get or create a new one
        ds, created = DataSource.objects.get_or_create(data_source_name=data_store, location=file_name)

        if not created:
            self.stdout.write(self.style.SUCCESS(f"Database already populated with datasource {ds}"))
            sys.exit()
        # populate indicators from first row
        Indicator.objects.bulk_create([indicator for indicator in indicator_factory(first)])

        # TODO: use country from inside the csv file
        geo = Geography.objects.get(id="NL")

        # populate all Entries with corresponding Indicators and create and Impact based on their relation.
        i = 0
        end = len(clean_data)
        with tqdm(total=end, unit_scale=True, unit_divisor=1, unit=" Entry") as pbar:
            while i < end:
                row = clean_data[i]
                ecoinvent = row[1].value.split(",")
                unit = row[2].value
                product_name = ecoinvent[0]
                ent = Entry.objects.create(product_name=product_name, unit=unit, geography=geo, data_source=ds)
                Impact.objects.bulk_create([impact for impact in impact_factory(row, ent)])
                i += 1
                pbar.update(i)
        self.stdout.write(self.style.SUCCESS("Successfully populated the database"))
