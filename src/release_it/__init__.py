"""
Copyright (c) 2022 Saransh Chopra. All rights reserved.

release_it: Automatically generate release notes!
"""


from __future__ import annotations

from release_it import extract  # noqa: F401
from release_it import nlp_backend  # noqa: F401
from release_it.high_level import (  # noqa: F401
    extract_release_comments,
    generate_release_notes,
)
from release_it.version import version as __version__  # noqa: F401
