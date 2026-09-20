import argparse

from mess_mood.data import load_reviews
from mess_mood.evaluate import fit, report

parser = argparse.ArgumentParser(prog="mess_mood", description="Is a canteen review positive or negative?")
commands = parser.add_subparsers(dest="command", required=True)
predict = commands.add_parser("predict", help="classify a review")
predict.add_argument("review")
commands.add_parser("evaluate", help="how good is the model?")
top = commands.add_parser("top-words", help="words that most suggest each label")
top.add_argument("-n", type=int, default=10)
args = parser.parse_args()

if args.command == "evaluate":
    report()
else:
    model = fit(load_reviews())
    if args.command == "predict":
        print(f"{model.predict(args.review)} ({model.confidence(args.review):.0%} sure)")
    else:
        for label in sorted(model.label_counts):
            print(f"{label}: {', '.join(model.top_words(label, args.n))}")
