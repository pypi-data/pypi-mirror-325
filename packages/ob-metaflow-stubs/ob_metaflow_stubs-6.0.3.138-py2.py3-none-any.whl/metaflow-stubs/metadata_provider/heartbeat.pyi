######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.9.2+obcheckpoint(0.1.7);ob(v1)                                                    #
# Generated on 2025-02-03T21:17:39.567558                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.exception

from ..exception import MetaflowException as MetaflowException

SERVICE_HEADERS: dict

HB_URL_KEY: str

class HeartBeatException(metaflow.exception.MetaflowException, metaclass=type):
    def __init__(self, msg):
        ...
    ...

class MetadataHeartBeat(object, metaclass=type):
    def __init__(self):
        ...
    def process_message(self, msg):
        ...
    @classmethod
    def get_worker(cls):
        ...
    ...

