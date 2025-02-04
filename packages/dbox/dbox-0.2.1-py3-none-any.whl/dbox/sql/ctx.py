from __future__ import annotations

import logging
from contextvars import ContextVar
from functools import cache
from pathlib import Path
from typing import List, Optional, Tuple

import jinja2

from dbox.ctx import set_context, use_factory, use_type

log = logging.getLogger(__name__)
parent_dir = Path(__file__).parent
JINJA_CTX: ContextVar[jinja2.Environment] = ContextVar("jinja")


@cache
def create_jinja(search_paths: Tuple[Path] = None) -> jinja2.Environment:
    log.info("Creating jinja environment with search paths: %s", search_paths)
    loader = jinja2.FileSystemLoader(searchpath=search_paths)
    jinja = jinja2.Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        loader=loader,
        undefined=jinja2.StrictUndefined,
    )
    return jinja


class SqlGenContext:
    def __init__(self):
        self._params = {}
        self._search_paths = (parent_dir / "templates",)

    @property
    def jinja(self) -> jinja2.Environment:
        return create_jinja(self._search_paths)

    def add_template_path(self, path: Path):
        self._search_paths = (*self._search_paths, path)

    def get_template(self, name: str = None, template_string: str = None) -> jinja2.Template:
        if template_string:
            return self.jinja.from_string(template_string)
        return self.jinja.get_template(name)

    def render_template(self, template: jinja2.Template | str, **kwargs) -> str:
        if isinstance(template, str):
            template = self.get_template(template)
        extra_params = {**self.params, "ctx": self}
        return template.render(**kwargs, **extra_params)

    @property
    def params(self):
        """Extra params for rendering templates."""
        return self._params

    def quote(self, identifier: str) -> str:
        # postgresql
        return f'"{identifier}"'

    def __enter__(self):
        self.__context_manager = set_sql_context(self)
        self.__context_manager.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return self.__context_manager.__exit__(exc_type, exc_value, traceback)


# re-export for type hinting
def use_sql_context():
    return use_type(SqlGenContext)


def set_sql_context(ctx: SqlGenContext):
    return set_context(SqlGenContext, ctx)


ExecutionContext = SqlGenContext
