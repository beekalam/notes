
### grub change timeout

	$ sudo vim /etc/default/grub 
	
and set the `GRUB_TIMEOUT`. 
-1 will disable it. And then run

	$ sudo update-grub

### starting windows in safe mode from grub

	for windows xp or 7 repeatedly press `F8` when you select the windows item.
	
### making windows usb boot in ubuntu

	$ sudo apt-get install unetbootin

### ubuntu installation

* for installattion make an `ext4` partition as the primary and a `swap` partition as logical drive.
* when ubuntu is installed run `sudo update-grub` if the windows is not shown in the grub boot list.

### listing broken packages?

	sudo apt-get check

### completely remove a package with configurations
	
	sudo apt-get purge <package_name>

### tell which package does a file belong to?
	
	dpkg -S libgthread-2.0.so.0
	
### deleting broken packages?

	* use synaptic package manager.
	* sudo dpkg -P package_name			# -P for purge

### installing apt-cacher-ng

add `00aptproxy` to `/etc/apt/apt.conf.d/` and add the following lines

	Acquire::http::Proxy "http://127.0.0.1:3142";


make `_import` folder in `/var/cache/apt-cache-ng/_import` copy your deb files in `_import` and
and goto `localhost:3142` and hit import.

### sudo timeout

	$ sudo visudo

add `Defaults timestamp_timeout=5` where 5 means 5 minutes which means sudo will remember your password
for 5 minutes

### installing postgresql in ubuntu 16.0

$ sudo apt-get install postgresql postgresql-contrib

 Now that we can connect to our PostgreSQL server, the next step is to set a password for the postgres user. Run the following command at a terminal prompt to connect to the default PostgreSQL template database:

sudo -u postgres psql template1

The above command connects to PostgreSQL database template1 as user postgres. Once you connect to the PostgreSQL server, you will be at a SQL prompt. You can run the following SQL command at the psql prompt to configure the password for the user postgres.

ALTER USER postgres with encrypted password 'your_password';


Upon installation Postgres is set up to use ident authentication, which means that it associates Postgres roles with
a matching Unix/Linux system account.

The installation procedure created a user account called postgres that is associated with the default Postgres role.
Switch over to the postgres account on your server by typing:

    sudo -i -u postgres

You can now access a Postgres prompt immediately by typing:

    psql


### Accessing a Postgres Prompt Without Switching Accounts

You can also run the command you'd like with the postgres account directly with sudo.

	$ sudo -u postgres psql

### php modules for connecting to postgresql

connecting to `postgresql` with `PDO`

	$ sudo apt-get install php-pgsql

Or if the package is installed, you need to enable the module in php.ini

extension=php_pgsql.dll (windows)
extension=php_pgsql.so (linux)

### phpstorm bad gateway in phpstorm

try installing

	$ sudo apt-get install php-cgi

### other useful php modules

	$ sudo apt-get install php-soap
	$ sudo apt-get install php-ssh2
	$ sudo apt-get install php-cli
	$ sudo apt-get install php-mbstring



### nodjs

How to install Node.js via binary archive on Linux?

Unzip the binary archive to any directory you wanna install Node, I use /usr/lib/nodejs

    sudo mkdir /usr/lib/nodejs
    sudo tar -xJvf node-v6.5.0-linux-x64.tar.xz -C /usr/lib/nodejs
    sudo mv node-v6.5.0-linux-x64 node-v6.5.0
    Set the environment variable ~/.profile, add below to the end

    # Nodejs
    export NODEJS_HOME=/usr/lib/nodejs/node-v6.5.0
    export PATH=$NODEJS_HOME/bin:$PATH

Test installation using

    $ node -v

    $ npm version

    the normal output is:

    ➜  nodejs node -v
    v6.5.0
    ➜  nodejs npm version
    { npm: '3.10.3',
    ares: '1.10.1-DEV',
    http_parser: '2.7.0',
    icu: '57.1',
    modules: '48',
    node: '6.5.0',
    openssl: '1.0.2h',
    uv: '1.9.1',
    v8: '5.1.281.81',
    zlib: '1.2.8' }
