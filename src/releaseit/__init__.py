"""
Copyright (c) 2022 Saransh Chopra. All rights reserved.

releaseit: Automatically generate release notes!
"""


from __future__ import annotations

from releaseit import extract  # noqa: F401
from releaseit import nlp_backend  # noqa: F401
from releaseit.high_level import (  # noqa: F401
    extract_release_comments,
    generate_release_notes,
)
from releaseit.version import version as __version__  # noqa: F401
