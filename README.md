/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

brew update

brew install postgres

postgres -D /usr/local/var/postgres


createdb 'tpch_sf1'

pg_restore -C -d 'tpch_sf1' /Users/weixie/Downloads/tpch_sf1.dump

createdb 'tpch_sf10'

pg_restore -C -d 'tpch_sf10' /Users/weixie/Downloads/tpch_sf10.dump


dropdb 'tpch_sf1'
dropdb 'tpch_sf10'


python generate_sql_query2.py

python generate_sql_query8.py

python process_sql_command_generator.py

chmod u+x *.sh

./process_sql_query2_command.sh

./process_sql_query8_command.sh

python generate_sql_query2.py

python generate_sql_query8.py

