from __future__ import annotations

from heapq import nlargest

import spacy
from sklearn.feature_extraction.text import TfidfVectorizer


def get_tfid_scores(comments: list[str]) -> dict[str, float]:
    v = TfidfVectorizer()
    v.fit(comments)
    v.transform(comments)

    all_feature_names = v.get_feature_names_out()
    word_score = {}

    for word in all_feature_names:
        indx = v.vocabulary_.get(word)
        word_score[word] = v.idf_[indx]

    return word_score


def generate_summary(
    comments: list[str],
    word_score: dict[str, float],
    output_filename: str = "RELEASE_NOTES.txt",
    model_name: str = "en_core_web_trf",
    threshold: float = 0.3,
) -> list[str]:
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
    summary = nlargest(select_length, sent_scores, key=sent_scores.get)  # type: ignore[arg-type]
    summary = [f"{sentence}\n" for sentence in summary]

    with open(output_filename, "w+") as f:
        f.writelines(summary)

    return summary
