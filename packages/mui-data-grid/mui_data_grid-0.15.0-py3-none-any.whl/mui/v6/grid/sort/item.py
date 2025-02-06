"""The item module holds the GridSortItem and related types."""

from __future__ import annotations

from pydantic import Field as PyField
from typing_extensions import TypeAlias

from mui.v6.grid.base import GridBaseModel
from mui.v6.grid.sort.direction import GridSortDirection, GridSortDirectionLiterals

Field: TypeAlias = str
# Sort and SortLiterals support "asc" | "desc" | null | undefined which we
# don't directly model
Sort: TypeAlias = "GridSortDirection | None"
SortLiterals: TypeAlias = "GridSortDirectionLiterals | None"


class GridSortItem(GridBaseModel):
    """Object that represents the column sorted data, part of the GridSortModel.

    Documentation:
        N/A

    Code:
        https://github.com/mui/mui-x/blob/0cdee3369bbf6df792c9228ef55ea1a61a246ff3/packages/grid/x-data-grid/src/models/gridSortModel.ts#L27-L39

    Attributes:
        field (str): The column field identifier.
        sort (GridSortDirection): The direction of the column that the grid should sort.
    """

    field: Field = PyField(
        default=...,
        title="Field",
        description="The direction of the column that the grid should sort.",
    )

    sort: Sort = PyField(
        default=...,
        title="Sort",
        description="The direction of the column that the grid should sort.",
    )
