######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.9.2+obcheckpoint(0.1.8);ob(v1)                                                    #
# Generated on 2025-02-07T01:44:39.600059                                                            #
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

