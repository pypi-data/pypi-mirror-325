######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.9.2+obcheckpoint(0.1.8);ob(v1)                                                    #
# Generated on 2025-02-07T01:44:39.568988                                                            #
######################################################################################################

from __future__ import annotations

import typing
import metaflow
if typing.TYPE_CHECKING:
    import metaflow.exception
    import metaflow

from ......exception import MetaflowException as MetaflowException
from .core import resolve_root as resolve_root

TYPE_CHECKING: bool

class UnresolvableDatastoreException(metaflow.exception.MetaflowException, metaclass=type):
    ...

def init_datastorage_object():
    ...

def resolve_storage_backend(pathspec: typing.Union[str, "metaflow.Task"] = None):
    ...

