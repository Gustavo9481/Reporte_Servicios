from typing import List
from pydantic import BaseModel
from . import models

class PaginatedReportsResponse(BaseModel):
    total_count: int
    reports: List[models.Reporte]