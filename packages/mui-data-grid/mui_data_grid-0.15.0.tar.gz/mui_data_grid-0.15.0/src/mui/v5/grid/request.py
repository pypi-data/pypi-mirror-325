"""The request module contains the model used to store parsed models."""

from __future__ import annotations

from datetime import timezone as dt_timezone
from typing import ClassVar
from zoneinfo import ZoneInfo

from pydantic import AliasChoices, ConfigDict, Field, field_validator

from mui.v5.grid.base import GridBaseModel, OptionalKeys
from mui.v5.grid.filter import GridFilterItem, GridFilterModel
from mui.v5.grid.link import GridLinkOperator
from mui.v5.grid.pagination import GridPaginationModel
from mui.v5.grid.sort import GridSortDirection, GridSortItem, GridSortModel


class RequestGridModels(GridBaseModel):
    """The x-data-grid models that are commonly sent to a server when requesting
    server-side enabled features.

    A grid model is a data structure used by the data grid to store the state of one
    aspect of it's features. For example, the GridFilterModel holds the data necessary
    to either filter the table's data or render the UI component responsible for
    controlling how the table's data is filtered.

    Attributes:
        filter_model (GridFilterModel): The filter model representing how to filter the
            table's data.
        pagination_model (GridPaginationModel): The pagination model representing how
            to paginate the table's data.
        sort_model (GridSortModel): The sort model representing how to sort the
            table's data.
    """

    filter_model: GridFilterModel = Field(
        default_factory=GridFilterModel,
        title="Filter Model",
        description="The filter model representing how to filter the table's data.",
        validation_alias=AliasChoices("filter_model", "filterModel"),
        examples=[
            GridFilterModel(
                items=[
                    GridFilterItem(
                        column_field="fieldName",
                        id=123,
                        operator_value="!=",
                        value="Field Value",
                    )
                ],
                link_operator=GridLinkOperator.And,
                quick_filter_logic_operator=None,
                quick_filter_values=None,
            )
        ],
    )
    pagination_model: GridPaginationModel = Field(
        default_factory=GridPaginationModel,
        title="Pagination Model",
        description=(
            "The pagination model representing how to paginate the table's data."
        ),
        validation_alias=AliasChoices("pagination_model", "paginationModel"),
        examples=[GridPaginationModel(page=3, page_size=30)],
    )
    sort_model: GridSortModel = Field(
        default_factory=list,
        title="Sort Model",
        description="The sort model representing how to sort the table's data.",
        validation_alias=AliasChoices("sort_model", "sortModel"),
        examples=[[GridSortItem(field="fieldName", sort=GridSortDirection.DESC)]],
    )
    timezone: ZoneInfo | dt_timezone | None = Field(
        default=None,
        title="Timezone",
        description="The timezone to apply to filtered data.",
        validation_alias=AliasChoices("timezone", "timeZone", "time_zone", "time-zone"),
        examples=["America/New_York"],
    )

    @field_validator("filter_model", mode="before")
    @classmethod
    def ensure_filter_model_isnt_none(cls, v: object) -> object:
        """Ensures that the key used the correct default when dynamically set."""
        return GridFilterModel() if v is None else v

    @field_validator("pagination_model", mode="before")
    @classmethod
    def ensure_pagination_model_isnt_none(cls, v: object) -> object:
        """Ensures that the key used the correct default when dynamically set."""
        return GridPaginationModel() if v is None else v

    @field_validator("sort_model", mode="before")
    @classmethod
    def ensure_sort_model_isnt_none(cls, v: object) -> object:
        """Ensures that the key used the correct default when dynamically set."""
        return [] if v is None else v

    _optional_keys: ClassVar[OptionalKeys] = {
        ("pagination_model", "paginationModel"),
        ("sort_model", "sortModel"),
        ("filter_model", "filterModel"),
        ("timezone",),
    }
    model_config = ConfigDict(arbitrary_types_allowed=True)
