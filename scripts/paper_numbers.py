"""Numbers of the paper: test cases only, case = mean over runs.
Usage: python scripts/paper_numbers.py results 1,2,3"""
import sys, json, importlib, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import numpy as np, pandas as pd
sys.path.insert(0, ROOT)
from req2code import stats
R = sys.argv[1]; runs = [int(x) for x in sys.argv[2].split(',')]
test = set(json.load(open(os.path.join(ROOT, 'data/my_dataset/splits.json')))['test'])
sc = pd.read_csv(f'{R}/scores_per_run.csv'); co = pd.read_csv(f'{R}/consistency_per_run.csv'); ti = pd.read_csv(f'{R}/timing_per_run.csv')
f = lambda d: d[d.case.isin(test) & d.run.isin(runs)]
sc, co, ti = f(sc), f(co), f(ti)
print('runs', runs, 'score rows', len(sc), 'cases', sc.case.nunique())
pc = sc.groupby(['condition','dataset','case','element'], as_index=False)['f1'].mean()
C = ['A','C','B','D','I','Q','O']
def m(el, ds):
    x = pc[(pc.element==el) & pc.dataset.isin(ds)]
    return {c: round(x[x.condition==c].f1.mean(),3) for c in C}, x[x.condition=='B'].case.nunique()
for name, el, ds in [('Class F1','classes',['D1','D2','D4']),('Attr F1','attributes',['D2','D4']),('Rel F1','relations',['D1','D2','D4']),
                     ('D1 UC','use_cases_provisional',['D1']),('eTour trace','trace_links',['D3']),('D1 class','classes',['D1']),
                     ('eTour UC','use_cases',['D3'])]:
    v,n = m(el, ds); print(f'{name:12s} n={n}', v)
cc = co.groupby(['condition','case'], as_index=False).mean(numeric_only=True)
for k in ['inconsistencies','inconsistency_rate','python_compiles','requirement_coverage','use_cases_without_method','actors_without_use_case']:
    if k in cc: print(f'{k:26s}', {c: round(cc[cc.condition==c][k].mean(),3) for c in C})
print(co.columns.tolist())
# tests: restrict relations/attributes to the datasets used in the paper
s1 = sc[((sc.element=='relations') & sc.dataset.isin(['D1','D2','D4'])) | ((sc.element=='attributes') & sc.dataset.isin(['D2','D4']))]
stats.RNG = np.random.default_rng(42)
r1 = stats.rq1(s1)
print(r1[['element','comparison','n','mean_first','mean_second','hl','ci_low','ci_high','r','p','p_holm']].to_string())
s2 = sc[(sc.element=='classes') & sc.dataset.isin(['D1','D2','D4'])]
r2, ni = stats.rq2(s2, co)
r2 = r2[r2.metric=='inconsistencies']
print(r2[['comparison','n','mean_S','mean_base','hl','ci_low','ci_high','r','p','p_holm']].to_string()); print(ni.to_string())
print('timing: tasks', len(ti), 'calls', ti.llm_calls.sum(), 'llm hours', round(ti.llm_seconds.sum()/3600,1), 'bad', ti.parse_failures.sum())
print(ti.groupby('condition').llm_calls.mean().round(1).to_dict())
# run-to-run variability: per-run mean of key metrics for B
for el, ds in [('classes',['D1','D2','D4']),('relations',['D1','D2','D4']),('attributes',['D2','D4'])]:
    x = sc[(sc.element==el)&sc.dataset.isin(ds)]
    print(el, x.groupby(['condition','run']).f1.mean().unstack().round(3).to_dict('index'))
