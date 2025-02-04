######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.9.2+obcheckpoint(0.1.7);ob(v1)                                                    #
# Generated on 2025-02-03T21:17:39.615498                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.exception

from ......exception import MetaflowException as MetaflowException

class LoadingException(metaflow.exception.MetaflowException, metaclass=type):
    def __init__(self, message):
        ...
    ...

class ModelException(metaflow.exception.MetaflowException, metaclass=type):
    def __init__(self, message):
        ...
    ...

