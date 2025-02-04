######################################################################################################
#                                 Auto-generated Metaflow stub file                                  #
# MF version: 2.13.9.1+obcheckpoint(0.1.7);ob(v1)                                                    #
# Generated on 2025-02-03T17:09:26.552909                                                            #
######################################################################################################

from __future__ import annotations

import metaflow
import typing
if typing.TYPE_CHECKING:
    import metaflow.plugins.pypi.conda_environment

from .conda_environment import CondaEnvironment as CondaEnvironment

class PyPIEnvironment(metaflow.plugins.pypi.conda_environment.CondaEnvironment, metaclass=type):
    ...

