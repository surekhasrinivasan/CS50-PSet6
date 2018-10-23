from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    a = set(a.split("\n"))
    b = set(b.split("\n"))

    return a & b


def sentences(a, b):
    """Return sentences in both a and b"""

    a = set(sent_tokenize(a))
    b = set(sent_tokenize(b))

    return a & b


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    return list(set(extract_substr(a, n)) & set(extract_substr(b, n)))


def extract_substr(a, n):
    """Return substrings of lenth n for a given string a"""

    return [a[i: i+n] for i in range(len(a) - (n - 1))]