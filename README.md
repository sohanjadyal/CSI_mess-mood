# mess-mood

Tells whether a canteen review is positive or negative. It's a Naive Bayes classifier written from scratch in plain Python, with no numpy and no scikit-learn, so you can read every step. It learns from about 100 reviews in `data/reviews.csv`.

## Running it

You need Python 3.10 or newer. `pytest` is the only thing to install, and only for the tests. On Windows the command is `python`.

```
python3 -m mess_mood predict "the dosa was cold and soggy"
python3 -m mess_mood evaluate
python3 -m mess_mood top-words
pip install -r requirements.txt && pytest
```

## How it works

1. `mess_mood/text.py` turns a review into words: lowercase, drop common words like "the", and join a negation to the next word (`not fresh` becomes `not_fresh`).
2. `mess_mood/model.py` counts how often each word shows up in positive and negative reviews, and uses those counts to score new reviews. The docstring at the top of the file has the formula.
3. `mess_mood/evaluate.py` measures how good the model is, on reviews it wasn't trained on.

## How it's supposed to work

- Punctuation and capital letters don't matter: `Good!`, `good` and `GOOD` are the same word.
- "not", "no" and "never" flip the meaning of the next word, so `not fresh` is treated differently from `fresh`.
- `evaluate` trains on 80% of the reviews and tests on the other 20%. The two sets never overlap.
- Precision for a label is: of the reviews the model gave that label, the share that really had it. Recall is: of the reviews that really had the label, the share the model found.
- In 5-fold cross-validation, every review is in exactly one test fold.

## Contributing

More reviews make a better model. Adding some to `data/reviews.csv`, with the text in quotes, is an easy first pull request.

For code changes, fork the repo, work on a new branch, run `pytest`, and open a pull request. If you find a bug, open an issue with the steps to reproduce it, what you expected, and what happened instead.

Part of Source Start by CSI SPIT. MIT licensed.
