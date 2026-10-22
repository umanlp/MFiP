import sys
from ast import literal_eval

parties = ['AfD', 'CDU', 'FDP', 'GRUENE', 'LINKE', 'SPD', 'fraktionslos']
affil, fnames, toks, ftypes, frames, mfs, tokspans = [], [], [], [], [], [], []

with open('MFiP_all_frames_with_negative_samples.tsv', 'r') as inf:
    for line in inf:
        elms = line.strip().split('\t')
        fnames.append(elms[0])
        toks.append(literal_eval(elms[1]))
        ftypes.append(elms[2])
        frames.append(elms[3])
        mfs.append(literal_eval(elms[4]))
        
for fname in fnames:
    for p in parties:
        if p in fname:
            affil.append(p)

dic = {p:{'toks':0, 'frames':0, 'MoralActOrGoal':0, 'ImmoralActOrGoal':0, 'MoralValue':0, 'ImmoralValue':0, 'PoliticalActOrGoal':0, 'NoFrame':0} for p in parties}

for i in range(len(fnames)):
    dic[affil[i]]['toks'] += len(toks[i])
    dic[affil[i]]['frames'] += 1
    dic[affil[i]][ftypes[i]] += 1


print('\\textbf{Party} & \\textbf{\# Tokens} &  \\textbf{\# Frames} &  \\textbf{MoralValue} &  \\textbf{MoralActOrGoal} &  \\textbf{ImmoralValue} &  \\textbf{ImmoralActOrGoal} &  \\textbf{PoliticalActOrGoal} & \\textbf{NoFrame} \\\\') 
print('\\hline')
for p in parties:
    print(p, "&", dic[p]['toks'], "&", dic[p]['frames'], "&", dic[p]['MoralValue'], "&", dic[p]['MoralActOrGoal'],"&", dic[p]['ImmoralValue'],"&", dic[p]['ImmoralActOrGoal'], "&", dic[p]['PoliticalActOrGoal'], "&", dic[p]['NoFrame'], "\\\\")
