"""
Copyright (c) 2022 Saransh Chopra. All rights reserved.

ReleaseIt: Automatically generate release notes!
"""


from __future__ import annotations

from releaseit.extract import (  # noqa: F401
    extract_additions,
    get_comments_and_docstrings,
    get_diff,
    preprocess_additions,
    save,
)
from releaseit.version import version as __version__  # noqa: F401
