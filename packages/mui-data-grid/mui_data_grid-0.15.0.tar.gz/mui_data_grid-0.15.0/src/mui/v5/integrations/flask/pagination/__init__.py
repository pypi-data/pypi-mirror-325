"""The pagination module contains the pagination model integration for Flask."""

from mui.v5.integrations.flask.pagination.model import (
    get_grid_pagination_model_from_request,
)

__all__ = ["get_grid_pagination_model_from_request"]
