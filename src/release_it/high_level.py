from __future__ import annotations

from release_it.extract import (
    extract_additions,
    get_comments_and_docstrings,
    get_diff,
    preprocess_additions,
)
from release_it.nlp_backend import get_release_notes, get_tfid_scores


def extract_release_comments(
    tags: list[str], path: str, output_filename: str
) -> list[str]:
    """
    A high-level API for extracting comments and docstrings added in between
    2 (ideally 2) tags or commits.

    Args:
        tags:
            A list of tags or commits (ideally 2 most recent) to find diff between.
        path:
            Path of the sub-directory to find the diff of.
        output_filename:
            Path of the file to store the diff in.

    Returns:
        comments:
            A list of comments and docstrings added in between the provided tags.
    """
    get_diff(tags, path, output_filename)
    extracted_additions = extract_additions(output_filename)
    preprocessed_additions = preprocess_additions(extracted_additions)
    comments = get_comments_and_docstrings(preprocessed_additions)

    return comments


def generate_release_notes(
    comments: list[str],
    output_filename: str = "RELEASE_NOTES.txt",
    model_name: str = "en_core_web_sm",
    threshold: float = 0.3,
) -> list[str]:
    word_score = get_tfid_scores(comments)
    release_notes = get_release_notes(
        comments, word_score, output_filename, model_name, threshold
    )

    return release_notes
