import json, pathlib
d = pathlib.Path('data')
fb  = json.loads((d/'facebook-santiam-hospital.json').read_text())['metrics']
ig  = json.loads((d/'instagram-santiam-hospital.json').read_text())['metrics']
fbc = json.loads((d/'facebook-family-birth-center.json').read_text())['metrics']
li  = json.loads((d/'linkedin-santiam-hospital.json').read_text())
MONTHS = ["2026-%02d"%m for m in range(1,9)]
LBL    = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug"]

def series(m,k): return [m[k]['months'][x] for x in MONTHS]

out = {}
out['months'] = LBL
out['fb']  = {'views':series(fb,'Views'),  'inter':series(fb,'Content interactions'),
              'follows':series(fb,'Follows'), 'visits':series(fb,'Visits'), 'clicks':series(fb,'Link clicks')}
out['ig']  = {'views':series(ig,'Views'),  'inter':series(ig,'Content interactions'),
              'follows':series(ig,'Follows'), 'visits':series(ig,'Visits'), 'clicks':series(ig,'Link clicks')}
out['fbc'] = {'views':series(fbc,'Views'), 'inter':series(fbc,'Content interactions'),
              'follows':series(fbc,'Follows'), 'visits':series(fbc,'Visits'), 'clicks':series(fbc,'Link clicks')}
out['li']  = {'views':[li['monthly']['impressions'][x] for x in MONTHS],
              'follows':[li['monthly']['new_followers'][x] for x in MONTHS],
              'er_own':[li['monthly']['engagement_rate_pct'][x] for x in MONTHS]}
li_inter = 412+5+11
out['li']['inter_total'] = li_inter

def tot(x): return sum(x)
rows=[]
for key,name,inter,views in [
    ('fb','Facebook — Santiam Hospital', tot(out['fb']['inter']), tot(out['fb']['views'])),
    ('ig','Instagram — Santiam Hospital', tot(out['ig']['inter']), tot(out['ig']['views'])),
    ('fbc','Facebook — Family Birth Center', tot(out['fbc']['inter']), tot(out['fbc']['views'])),
    ('li','LinkedIn — Santiam Hospital', li_inter, tot(out['li']['views'])),
    ('x','X — @SantiamHospital', 3, 470)]:
    rows.append((name, views, inter, round(inter/views*100,2)))

out['summary']=rows
tv = sum(r[1] for r in rows); ti = sum(r[2] for r in rows)
out['grand']={'views':tv,'inter':ti,'er':round(ti/tv*100,2),
  'new_follows': tot(out['fb']['follows'])+tot(out['ig']['follows'])+tot(out['fbc']['follows'])+tot(out['li']['follows'])}

# monthly engagement rate per platform (interactions / views)
for k in ['fb','ig','fbc']:
    out[k]['er']=[round(i/v*100,2) if v else 0 for i,v in zip(out[k]['inter'],out[k]['views'])]
out['li']['er']=[round(i/v*100,2) for i,v in zip(
    [ round(li_inter*x/sum(out['li']['views']),2) for x in out['li']['views'] ], out['li']['views'])]

print(json.dumps(out['summary'],indent=1))
print('GRAND', out['grand'])
print('FB ER', out['fb']['er'])
print('IG ER', out['ig']['er'])
print('FBC ER', out['fbc']['er'])
print('LI own ER', out['li']['er_own'])
pathlib.Path('data/computed.json').write_text(json.dumps(out,indent=1))
