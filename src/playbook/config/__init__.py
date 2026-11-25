"""Configuration for the playbook package.

Public interface::

    from playbook.config import load_settings

    settings = load_settings()
    settings.general.catalog
    settings.ml.chat_endpoint
"""

from playbook.config.loader import load_settings
from playbook.config.models import EtlSettings, GeneralSettings, MlSettings, Settings

__all__ = [
    "EtlSettings",
    "GeneralSettings",
    "MlSettings",
    "Settings",
    "load_settings",
]
