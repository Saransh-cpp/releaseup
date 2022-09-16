"""
Copyright (c) 2022 Saransh Chopra. All rights reserved.

releaseup: Automatically generate release notes!
"""


from __future__ import annotations

from releaseup import extract  # noqa: F401
from releaseup import nlp_backend  # noqa: F401
from releaseup.high_level import (  # noqa: F401
    extract_release_comments,
    generate_release_notes,
)
from releaseup.version import version as __version__  # noqa: F401
