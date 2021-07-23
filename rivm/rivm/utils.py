import os
import re
from collections import namedtuple

EntryRow = namedtuple("EntryRow", "header, unit, value")
header_patters = re.compile("[a-zA-Z0-9 _-]+:[a-zA-Z0-9 _-]+:[a-zA-Z0-9 _-]+")  # TODO: Add pattern for ecoinvent


def transform_to_entry(item):
    return EntryRow(item[0], item[1], item[2])


def not_valid(item: EntryRow):
    if header_patters.findall(
            item.header) or "Data source" in item.header or "Ecoinvent" in item.header or "Unit" in item.header:
        return item


def indicator_only(item: EntryRow):
    if header_patters.findall(item.header):
        return item.header


def get_results(result):
    for i, _ in enumerate(result):
        if i > 2:
            yield list(zip(result[0], result[1], result[i]))


def transform_to_entry_factory(result):
    for row in result:
        yield list(map(transform_to_entry, row))


def remove_invalid_rows(result):
    for row in result:
        yield list(filter(not_valid, row))


def get_abs_path(file_name: str, dir_name: str = None):
    p_root = os.path.dirname(os.path.abspath(os.path.join(dir_name, file_name)))
    return os.path.join(p_root, file_name)


def file_path_and_mode(path: str, mode="r"):
    dir_name, file_name = os.path.split(path)
    return get_abs_path(file_name, dir_name), mode
