### setting up DHCP for freebsd in virtual box

	hostname="plato.myhostname.com"
	ifconfig_xl0="DHCP"

where `xl0` is the name of the interface.

### setting up static ip

	ifconfig_xl0="inet 192.168.0.53 netmask 255.255.255.0"
	defaultrouter="192.168.0.1"
	hostname="plato.myhostname.com"

### Multiple IPs on one network card

	ifconfig_xl0="inet 192.168.0.53 netmask 255.255.255.0"
	ifconfig_xl0_alias0="inet 192.168.0.54 netmask 255.255.255.0"
	ifconfig_xl0_alias1="inet 192.168.0.55 netmask 255.255.255.0"
	defaultrouter="192.168.0.1"
	hostname="plato.myhostname.com"

### Set IP address useing ifconfig command:

	ifconfig re0 inet 202.54.1.22

### installing package manager.

just type `pkg`

### starting `sshd`

FreeBSD has OpenSSH-server installed by default.
Enable it with sshd_enable="YES" in rc.conf, and run "sh /etc/rc.d/sshd start"

check for status:

	/etc/rc.d/sshd status

### ssh into virtual machine

use bridging instead of NAT.
and you should enable `PermitRootLogin` in `/etc/ssh/sshd_config`
	
	PermitRootLogin yes


### searching packages with pkg

	$ pkg search <packagename>

### installing postgresql

	$ pkg install postgresql-<version>
	$ /usr/local/etc/rc.d/postgresql initdb
	$ /usr/local/etc/rc.d/postgresql start

the default user created when you install `postgresql` in Freebsd is `pgsql`

	$ su pgsql

logs in as pgsql.

__ADDING root user to postgresql login__

	$ su pgsql
	$ createuser --interactive

__REMOVING role__

	$ su pgsql
	$ drop role <rolename>


### restoring database with pg_restore

	pg_restore -h localhost -p 5432 -U root -C -d mydb ./mydb.custom

-C creates the datbase
-d connects to the database

### switching between databases in psql

	\connect DBNAME

### use scp to move files

	scp -r /tmp/backupmanager root@192.168.1.103:/root/

### install bash on freebsd

	pkg install bash

### running bash scripts 

	bash /path/bashfile.sh

### cron jobs

cron has its own environment.So make sure to add additional paths to cron
when you issue `crontab -e` on top of the file.

	PATH=/sbin:/bin:/usr/sbin:/usr/bin

If you need default system wide PATHs and other ENV variables
 (which defined in /etc/profile.d), just put the following:

	* * * * * . /etc/profile; your cmd



