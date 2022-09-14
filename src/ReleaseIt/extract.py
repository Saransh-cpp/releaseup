import subprocess


def get_diff(commits, path, filename):
    subprocess.run(["git", "diff", commits[0], commits[1], path, ">", filename])


def extract_additions(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        extracted_additions = [line for line in lines if line[0] == "+"]

    return extracted_additions


def preprocess_additions(extracted_additions):
    preprocessed_additions = extracted_additions.copy()
    for line in preprocessed_additions:
        if line[:3] == "+++":
            preprocessed_additions.pop(preprocessed_additions.index(line))

    preprocessed_additions = [line[1:] for line in preprocessed_additions]
    preprocessed_additions = [f"{line.strip()}\n" for line in preprocessed_additions]

    return preprocessed_additions


def get_comments_and_docstrings(preprocessed_additions):
    comments_and_docstrings = [
        line[line.find("#") + 1 :].replace("\n", "").strip()
        for line in preprocessed_additions
        if "#" in line
    ]
    lines = " ".join(preprocessed_additions).replace("\n", " ")
    i = 0

    while i < len(lines):
        if lines[i : i + 3] == '"""':
            idx = lines[i + 3 :].find('"""')
            comments_and_docstrings.append(lines[i + 3 : i + idx + 3])
            i += idx + 6
            continue
        i += 1

    return [f"{x.strip()}\n" for x in comments_and_docstrings]


def save(content, filename):
    with open(filename, "w") as f:
        f.write("".join(content))


# if __name__ == "__main__":
#     extracted_additions = extract_additions("diff.txt")
#     preprocessed_additions = preprocess_additions(extracted_additions)
#     comments_and_docstrings = get_comments_and_docstrings(preprocessed_additions)
#     save(comments_and_docstrings, "docs.txt")
