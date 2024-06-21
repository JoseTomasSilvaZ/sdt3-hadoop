#!/bin/bash

set -e
apt-get update
apt-get install -y postgresql postgresql-contrib
service postgresql start 

sudo -u postgres psql <<EOF
CREATE DATABASE metastore_db;
CREATE USER hiveuser WITH ENCRYPTED PASSWORD 'hivepassword';
GRANT ALL PRIVILEGES ON DATABASE metastore_db TO hiveuser;
\q
EOF
echo "PSQL Setup OK"

cat <<EOL > "/usr/local/apache-hive-2.3.5-bin/conf/hive-site.xml"
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<configuration>
  <property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:postgresql://localhost/metastore_db</value>
    <description>JDBC connect string for a JDBC metastore</description>
  </property>

  <property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>org.postgresql.Driver</value>
    <description>Driver class name for a JDBC metastore</description>
  </property>

  <property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>hiveuser</value>
    <description>Username to use against metastore database</description>
  </property>

  <property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>hivepassword</value>
    <description>Password to use against metastore database</description>
  </property>
</configuration>
EOL
schematool -initSchema -dbType postgres

echo "Hive + PSQL OK"
