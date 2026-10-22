# MFiP: Moral Frames in Politics

This github provides supplementary materials for our EMNLP-2025 paper:

"Moral Framing in Politics (MFiP): A new resource and models for moral framing"

```
@inproceedings{rehbein-etal-2025-moral-framing,
    title = "Moral Framing in Politics ({MF}i{P}): A new resource and models for moral framing",
    author = "Rehbein, Ines  and
      Reinig, Ines  and
      Ponzetto, Simone Paolo",
    editor = "Christodoulopoulos, Christos  and
      Chakraborty, Tanmoy  and
      Rose, Carolyn  and
      Peng, Violet",
    booktitle = "Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing",
    month = nov,
    year = "2025",
    address = "Suzhou, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.emnlp-main.1757/",
    doi = "10.18653/v1/2025.emnlp-main.1757",
    pages = "34643--34663",
    ISBN = "979-8-89176-332-6",
}
```


The repository includes the data and annotation guidelines for the MFiP corpus.


## Data 

In the data folder are two subfolders. The first one, ```mfip```, includes the annotation layers in a json format, with labels annotated by the individual coders and the majority label (see paper for details).

The second folder, ```xval```, includes the preprocessed data used in the crossvalidation experiments described in the paper.


## Frame identification (FI)

- only used to extract data for data augmentation
- no experimental results reported in the paper (only baseline in appendix, see Appendix D, Moral frame identification (FI))


## Frame classification (FC)


| Frame type distribution |
|---------------------|
|      45 ImmoralValue |
|     475 MoralValue |
|   1,090 NoFrame |
|   1,314 PoliticalActOrGoal |
|   2,262 ImmoralActOrGoal |
|   2,386 MoralActOrGoal |
| |
|   7,572 Total |


### Compute distribution of frames per party (outputs a latex table) 

cd MFiP/experiments/data/xval

- create train/test sets for 5-fold cross-validation

bash make_train_test.sh

python stats.py

|Party | # Tokens |  # Frames |  MoralValue |  MoralActOrGoal |  ImmoralValue |  ImmoralActOrGoal |  PoliticalActOrGoal | NoFrame |
|-------|-------|-------|-------|-------|-------|-------|-------|-------|
| AfD | 71275 | 1193 | 68 | 272 | 8 | 541 | 157 | 147 |
| CDU | 161447 | 2218 | 145 | 747 | 6 | 467 | 446 | 407 |
| FDP | 47565 | 799 | 46 | 282 | 1 | 204 | 153 | 113 |
| GRUENE | 40956 | 653 | 53 | 180 | 10 | 222 | 115 | 73 |
| LINKE | 46308 | 868 | 36 | 220 | 2 | 396 | 107 | 107 |
| SPD | 119938 | 1771 | 123 | 664 | 16 | 403 | 324 | 241 |
| fraktionslos | 6562 | 70 | 4 | 21 | 2 | 29 | 12 | 2 |


Please also see our repo with the final release of the corpus, including unified annotation layers for the parliamentary debates (NER, Situation Entities, Speech Events, MoPE annotations, and moral frames/roles). The corpus includes all annotation layers in a unified json format:

**Github:**  https://github.com/umanlp/gepadeu.git

You can also search a pre-final version of the corpus online (w/o roles, to be added soon). The corpus is available via the ANNIS platform, an open source web browser-based search and visualisation architecture for complex multilevel linguistic corpora with diverse types of annotation. [See here for more info on ANNIS](https://corpus-tools.org/annis/). 

**GePaDeU in ANNIS:** [Search the corpus online](https://linguistischeempirieannis.uni-muenster.de/annis/#_q=c3BlZWNoYWN0PSJEZW1hbmQiIF9pXyAiRnJlaWhlaXQi&ql=aql&_c=R2VQYURlVQ&cl=5&cr=5&s=0&l=10).


**Paper:**

```
@inproceedings{rehbein-etal-2026-gepadeu,
    title = "{G}e{P}a{D}e{U} - a Multi-layer Corpus of {G}erman Parliamentary Debates with Rich Semantic and Pragmatic Annotations",
    author = "Rehbein, Ines  and
      Schlenker, Julian  and
      Ostertag, Lars  and
      Ponzetto, Simone Paolo",
    editor = "Piperidis, Stelios  and
      Bel, N{\'u}ria  and
      van den Heuvel, Henk  and
      Ide, Nancy  and
      Krek, Simon  and
      Toral, Antonio",
    booktitle = "Proceedings of the Fifteenth Language Resources and Evaluation Conference",
    month = may,
    year = "2026",
    address = "Palma de Mallorca, Spain",
    publisher = "ELRA Language Resource Association",
    url = "https://aclanthology.org/2026.lrec-1.141/",
    doi = "10.63317/5d28ibqd2nzk",
    pages = "1794--1810",
}
```



