# lexicon-sentiment-analysis
Simple example of using a lexicon to perform sentiment analysis

# Usage

```
python ./doAnalysis.py
```

# The lexicon

Included in this repository is a lexicon is the [MPQA subjectivity lexicon](http://mpqa.cs.pitt.edu/lexicons/subj_lexicon/). See the file `subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.README` for more information.

I've created a simpler format of the lexicon, using the `subjectivity_clues_hltemnlp05/reformat.py` script. The resulting file is ``subjectivity_clues_hltemnlp05/lexicon_easy.csv`,
and that's what the `doAnalysis.py` script uses.

# Data

Included in this repository is a dataset of tweets. Each row contains three columns:

1. The tweet text.
2. The tweet ID.
3. The tweet publish date

The full dataset (i.e., `newtwitter.csv` contains 8,595 rows. A small sample of 100 rows (i.e., `newtwitter.small.csv`) is also provided.



