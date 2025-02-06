from typing import List, Protocol, Tuple

from validata_core.domain.types.source import Header, InlineArrayOfArrays, Row


class TableReader(Protocol):
    def read_header_and_rows(self) -> Tuple[Header, list[Row]]: ...

    def source(self) -> str: ...


class ValidataResource:
    def __init__(self, reader: TableReader):
        self._reader = reader

        header, rows = reader.read_header_and_rows()

        self._header: Header = header
        self._rows: List[Row] = rows

    @property
    def n_rows(self) -> int:
        return len(self._rows)

    @property
    def n_fields(self) -> int:
        return len(self._header)

    def source(self) -> str:
        return self._reader.source()

    def header(self) -> Header:
        return self._header

    def rows(self) -> List[Row]:
        return self._rows

    def to_inline_data(self) -> InlineArrayOfArrays:
        return [self.header()] + self.rows()

    @staticmethod
    def is_supported_type(extension: str) -> bool:
        if extension and extension[0] != ".":
            extension = "." + extension
        return extension in (".csv", ".tsv", ".ods", ".xls", ".xlsx")
