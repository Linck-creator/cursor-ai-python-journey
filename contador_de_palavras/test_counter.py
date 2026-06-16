"""Module for counting word frequencies and providing utility unit tests.

This module contains the WordCounter class for counting word frequencies
from an iterable of words, along with associated utility methods and a test function.

Optimization Notes:
-------------------
1. Counter construction: O(N) time, where N is the number of words.
   Each word is added to a dictionary, which has amortized O(1) insertion time.
   This step is already optimal for counting.

2. Lookup of individual word frequency: O(1) time, since Counter is a dictionary subclass.

3. Finding the 'n' most common words:
   The standard Counter.most_common(n) method calls heapq.nlargest,
   which is O(N log n), where N is the number of unique words.
   For small n (e.g., n=10), this is efficient. A full sort would be O(K log K),
   where K is the number of unique words.

Possible Optimization:
- If you need only single/multiple queries for the most common words, current implementation is
  efficient.
- For repeated queries with different n, consider precalculating the sorted list once
  (O(K log K)) if K is not huge.
- For very large files, read and process the file in chunks to avoid memory issues.

Overall, the present algorithm is near-optimal for most word counting situations.
"""

from collections import Counter
from collections.abc import Iterable
from typing import List, Tuple


class WordCounter:
    """
    A class used to count word frequencies in a list of words.

    Attributes
    ----------
    words : List[str]
        The list of words to be counted.
    counter : Counter
        The Counter that tallies word frequencies.

    Methods
    -------
    count(word: str) -> int:
        Returns the frequency count of the provided word.
    most_common(n: int = 10) -> List[Tuple[str, int]]:
        Returns a list of the n most frequent words and their counts.
    """

    def __init__(self, words: Iterable[str]):
        """
        Initializes the WordCounter with an iterable of words.

        Parameters
        ----------
        words : Iterable[str]
            A sequence of words to be counted.
        """
        self.words: List[str] = list(words)
        self.counter: Counter = Counter(self.words)

    def count(self, word: str) -> int:
        """
        Returns the count of the specified word.

        Parameters
        ----------
        word : str
            The word for which the frequency is requested.

        Returns
        -------
        int
            The frequency of the provided word.
        """
        return self.counter[word]

    def most_common(self, n: int = 10) -> List[Tuple[str, int]]:
        """
        Returns the n most common words and their frequencies.

        Parameters
        ----------
        n : int, optional
            The number of top items to return (default is 10).

        Returns
        -------
        List[Tuple[str, int]]
            A list of word-frequency pairs in descending order of frequency.
        """
        return self.counter.most_common(n)


def test_word_counter() -> None:
    """
    Unit tests for the WordCounter class.
    Verifies counting and most_common methods.
    """
    words = ["python", "python", "ai"]
    wc = WordCounter(words)

    assert wc.count("python") == 2
    assert wc.count("ai") == 1
    assert wc.most_common(2) == [("python", 2), ("ai", 1)]
