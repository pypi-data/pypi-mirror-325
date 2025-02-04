######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.9.1+obcheckpoint(0.1.7);ob(v1)                                                    #
# Generated on 2025-02-03T17:09:26.610306                                                            #
######################################################################################################

from __future__ import annotations

import typing
if typing.TYPE_CHECKING:
    import typing


class SerializationHandler(object, metaclass=type):
    def serialze(self, *args, **kwargs) -> typing.Union[str, bytes]:
        ...
    def deserialize(self, *args, **kwargs) -> typing.Any:
        ...
    ...

