sudo -u postgres dropdb eia >> /dev/null
sudo -u postgres dropuser eia >> /dev/null
sudo -u postgres createuser eia
sudo -u postgres createdb eia
sudo -u postgres psql << EOF
alter user eia with encrypted password 'eiae123';
alter role eia set client_encoding to 'utf8';
alter role eia set default_transaction_isolation to 'read committed';
alter role eia set timezone to 'utc';
alter role eia createdb;
grant all privileges on database eia to eia ;\q
EOF
