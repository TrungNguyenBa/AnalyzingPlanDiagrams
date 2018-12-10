import os

folder_name = 'sql_query2'
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)

query_head = '''EXPLAIN (FORMAT JSON) select
    s_acctbal,
    s_name,
    n_name,
    p_partkey,
    p_mfgr,
    s_address,
    s_phone,
    s_comment
from
    part,
    supplier,
    partsupp,
    nation,
    region
where
    p_partkey = ps_partkey
    and s_suppkey = ps_suppkey
    and p_type like 'BRASS'
    and s_nationkey = n_nationkey
    and n_regionkey = r_regionkey
    and r_name = 'EUROPE'
'''

query_tail='''
order by
    s_acctbal desc,
    n_name,
    s_name,
    p_partkey;
'''

p_max = 50.0
p_min = 1.0
p_step = (p_max-p_min)/100
ps_max = 1000.0
ps_min = 1.0
ps_step = (ps_max-ps_min)/100

for p in range(0,101):
    for ps in range(0,101):
        file_name = 'query2p{}_ps{}.sql'.format(p,ps)
        query_middle = '    and p_size<={}\n    and ps_supplycost<={}'.format(p_min+p*p_step,ps_min+ps*ps_step)
        with open(os.path.join(folder_name,file_name),'w') as f:
            f.write(query_head+query_middle+query_tail)
