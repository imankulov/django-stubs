from typing import Any, Callable, Iterable

from django.db import IntegrityError
from django.db.models.fields import Field
from django.db.models.options import Options

def CASCADE(collector, field, sub_objs, using): ...
def SET_NULL(collector, field, sub_objs, using): ...
def SET_DEFAULT(collector, field, sub_objs, using): ...
def DO_NOTHING(collector, field, sub_objs, using): ...
def PROTECT(collector, field, sub_objs, using): ...
def SET(value: Any) -> Callable: ...
def get_candidate_relations_to_delete(opts: Options) -> Iterable[Field]: ...

class ProtectedError(IntegrityError): ...

class Collector:
    def __init__(self, using: str) -> None: ...
