import csv
import sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ROOT)

from RAscore import RAscore_XGB

xgb_scorer = RAscore_XGB.RAScorerXGB()

infile = sys.argv[1]
outfile = sys.argv[2]

smiles = []
with open(infile, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        smiles += [r[0]]

preds = []
for smi in smiles:
    preds += [xgb_scorer.predict(smi)]

with open(outfile, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["ra_score"])
    for p in preds:
        writer.writerow([p])
