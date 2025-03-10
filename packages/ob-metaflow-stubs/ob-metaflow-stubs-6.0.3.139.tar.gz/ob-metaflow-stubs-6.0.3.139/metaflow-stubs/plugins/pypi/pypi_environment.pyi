######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.9.2+obcheckpoint(0.1.8);ob(v1)                                                    #
# Generated on 2025-02-07T01:44:39.578527                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.plugins.pypi.conda_environment

from .conda_environment import CondaEnvironment as CondaEnvironment

class PyPIEnvironment(metaflow.plugins.pypi.conda_environment.CondaEnvironment, metaclass=type):
    ...

