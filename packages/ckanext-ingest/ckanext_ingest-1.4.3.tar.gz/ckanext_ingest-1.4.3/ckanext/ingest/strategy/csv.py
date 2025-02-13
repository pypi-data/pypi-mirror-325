from __future__ import annotations

import csv
import logging
from io import StringIO
from typing import Any, Iterable

from ckanext.ingest import shared
from ckanext.ingest.record import PackageRecord

log = logging.getLogger(__name__)


class CsvSimpleStrategy(shared.ExtractionStrategy):
    """Extract records from CSV."""

    mimetypes = {"text/csv"}

    def chunks(
        self,
        source: shared.Storage,
        options: shared.StrategyOptions,
    ) -> Iterable[dict[str, Any]]:
        reader_options: dict[str, Any] = shared.get_extra(options, "reader_options", {})
        str_stream = StringIO(source.read().decode())

        return csv.DictReader(str_stream, **reader_options)

class CsvStrategy(CsvSimpleStrategy):
    """Transform CSV records into datasets using ckanext-scheming.

    Every scheming field that has `ingest_options` attribute defines how data
    from the row maps into metadata schema. For example, if `notes` field has
    `ingest_options: {aliases: [DESCRIPTION]}`, `DESCRIPTION` column from CSV
    will be used as a data source for this field.

    """
    record_factory = PackageRecord
