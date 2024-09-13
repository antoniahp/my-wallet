from dataclasses import dataclass
from datetime import date
from typing import Optional

from cqrs.queries.query import Query


@dataclass(frozen=True)
class GetFilteredCommissionsCalculatedQuery(Query):
    # country: Optional[List] = None
     date__gte: date
     date__lte: date
