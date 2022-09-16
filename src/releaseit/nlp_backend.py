from __future__ import annotations

from heapq import nlargest

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer


def get_tfid_scores(comments: list[str]) -> dict[str, float]:
    """
    Extract TF-IDF scores for a list of strings.

    Args:
        comments:
            Strings for the TF-IDF score.

    Returns:
        word_score:
            A dict of words mapped to their TF-IDF scores.
    """
    v = TfidfVectorizer()
    v.fit(comments)
    v.transform(comments)

    all_feature_names = v.get_feature_names_out()
    word_score = {}

    for word in all_feature_names:
        indx = v.vocabulary_.get(word)
        word_score[word] = v.idf_[indx]

    return word_score


def get_release_notes(
    comments: list[str],
    word_score: dict[str, float],
    output_filename: str = "RELEASE_NOTES.txt",
    model_name: str = "en_core_web_sm",
    threshold: float = 0.3,
) -> list[str]:
    """
    Generate release_notes (or release notes) from the extracted
    comments and TF-IDF scores.

    Args:
        comments:
            A list of extracted comments.
        word_score:
            A dict of words mapped to their TF-IDF scores.
        output_filename:
            Path of the file where release notes are to be dumped.
        model_name:
            spacy's model name. See https://spacy.io/usage/models.
        threshold:
            Percentage of comments to be included in the release notes.

    Returns:
        release_notes:
            Release notes a s a list of strings.
    """
    nlp = spacy.load(model_name)

    comments_str = " ".join(comments).replace("\n", "")
    doc = nlp(comments_str)
    sentences = list(doc.sents)
    sent_scores: dict[str, float] = {}

    for sent in sentences:
        for word in sent:
            if word.text.lower() in word_score.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_score[word.text.lower()]
                else:
                    sent_scores[sent] += word_score[word.text.lower()]

    select_length = int(len(sentences) * 0.3)
    release_notes = nlargest(select_length, sent_scores, key=sent_scores.get)  # type: ignore[arg-type]
    release_notes = [f"{sentence}\n" for sentence in release_notes]

    with open(output_filename, "w+") as f:
        f.writelines(release_notes)

    return release_notes
