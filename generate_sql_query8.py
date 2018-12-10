import os

folder_name = 'sql_query8'
if not os.path.isdir(folder_name):
    os.mkdir(folder_name)

query_head = '''EXPLAIN (FORMAT JSON) select
    o_year,
    sum(case
    when nation = 'CANADA'
    then volume
    else 0
    end) / sum(volume) as mkt_share
from (
    select
        extract(year from o_orderdate) as o_year,
        l_extendedprice * (1-l_discount) as volume,
        n2.n_name as nation
    from
        part,
        supplier,
        lineitem,
        orders,
        customer,
        nation n1,
        nation n2,
        region
    where
        p_partkey = l_partkey
        and s_suppkey = l_suppkey
        and l_orderkey = o_orderkey
        and o_custkey = c_custkey
        and c_nationkey = n1.n_nationkey
        and n1.n_regionkey = r_regionkey
        and r_name = 'AMERICA'
        and s_nationkey = n2.n_nationkey
        and o_orderdate between date '1995-01-01' and date '1996-12-31'
        and p_type = 'SMALL BURNISHED STEEL'
'''

query_tail='''
    ) as all_nations
group by
    o_year
order by
    o_year;
'''

s_max = 9999.72
s_min = -998.22
s_step = (s_max-s_min)/100
l_max = 50.0
l_min = 1
l_step = (l_max-l_min)/100

for s in range(0,101):
    for l in range(0,101):
        file_name = 'query8s{}_l{}.sql'.format(s,l)
        query_middle = '        and s_acctbal<={}\n        and l_quantity<={}'.format(s_min+s*s_step,l_min+l*l_step)
        with open(os.path.join(folder_name,file_name),'w') as f:
            f.write(query_head+query_middle+query_tail)
