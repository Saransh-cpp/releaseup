from __future__ import annotations

import subprocess


def get_diff(
    commits: list[str], path: str = "./", output_filename: str = "diff.txt"
) -> None:
    """
    Writes `git diff` to a file.

    Args:
        commits:
            A list of commits (ideally 2 most recent) to find diff between.
        path:
            Path of the sub-directory to find the diff of.
        output_filename:
            Path of the file to store the diff in.
    """
    with open(output_filename, "w+") as f:
        subprocess.run(["git", "diff", commits[0], commits[1], "--", path], stdout=f)


def extract_additions(filename: str) -> list[str]:
    """
    Extracts all the additions made to a codebase from a file containing `git diff`.

    Args:
        filename:
            File containing the `git diff`.

    Returns:
        extracted_additions:
            A list of additions made to the codebase.
    """
    with open(filename) as f:
        lines = f.readlines()
        extracted_additions = [line for line in lines if line[0] == "+"]

    return extracted_additions


def preprocess_additions(extracted_additions: list[str]) -> list[str]:
    """
    Preprocesses the extracted additions from `git diff`.

    Args:
        extracted_additions:
            A `git diff` containing only the additions.

    Returns:
        preprocessed_additions:
            Preprocessed additions.
    """
    preprocessed_additions = extracted_additions.copy()
    preprocessed_additions = [f"{line.strip()}\n" for line in preprocessed_additions]
    for line in preprocessed_additions:
        if line[:3] == "+++":
            preprocessed_additions.pop(preprocessed_additions.index(line))

    preprocessed_additions = [line[1:] for line in preprocessed_additions]
    preprocessed_additions = [f"{line.strip()}\n" for line in preprocessed_additions]

    return preprocessed_additions


def get_comments_and_docstrings(preprocessed_additions: list[str]) -> list[str]:
    """
    Extracts comments and docstrings from preprocessed `git diff` output.

    Args:
        preprocessed_additions:
            A list of preprocessed additions from `git diff`.

    Returns:
        extracted_docs:
            Extracted comments and docstrings from the preprocessed_additions.
    """
    comments_and_docstrings = [
        line[line.find("#") + 1 :].replace("\n", "").strip()
        for line in preprocessed_additions
        if "#" in line
    ]
    lines = " ".join(preprocessed_additions).replace("\n", " ")
    i = 0

    while i < len(lines):
        if lines[i : i + 3] == '"""':
            idx_next_quotes = lines[i + 3 :].find('"""')
            # args = lines[i + 3 :].find('Args:') if lines[i + 3 :].find('Args:') != -1 else sys.maxsize
            # returns = lines[i + 3 :].find('Returns:') if lines[i + 3 :].find('Returns:') != -1 else sys.maxsize
            # examples = lines[i + 3 :].find('Examples:') if lines[i + 3 :].find('Examples:') != -1 else sys.maxsize
            # idx = min(args, returns, examples)
            # if idx != sys.maxsize:
            comments_and_docstrings.append(lines[i + 3 : i + idx_next_quotes + 3])
            i += idx_next_quotes + 6
            continue
        i += 1

    extracted_docs = [x.strip() for x in comments_and_docstrings]
    extracted_docs = [doc.replace("\n", "").replace("\t", "") for doc in extracted_docs]
    extracted_docs = [f"{x.strip()}\n" for x in comments_and_docstrings]

    i = 0
    while i < len(extracted_docs):
        line = extracted_docs[i]
        if "noqa" in line or "type:" in line or line == "\n" or "todo" in line.lower():
            extracted_docs.pop(i)
        else:
            i += 1

    return extracted_docs


def save(content: list[str], filename: str) -> None:
    """
    Save contents in a file.

    Args:
        content:
            A list of contents to be saved.
        filename:
            Path of the file in which the contents have to be saved
    """
    with open(filename, "w+") as f:
        f.write("".join(content))
