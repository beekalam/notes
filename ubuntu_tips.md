[time](#time)

### remap caps lock to ctrl

To permanently change the behaviour:

    run dconf-editor

    select org.gnome.desktop.input-sources

    Change xkb-options to ['ctrl:nocaps'] (or add it to any existing options)

or on the command line (Warning -- this overwrites your existing settings!):

gsettings set org.gnome.desktop.input-sources xkb-options "['ctrl:nocaps']"

### how teo tell which version of library you have?

	$ dpkg -l '*ssh*'

### groups

### Add a New Group

To add a new group, all you need to do is use the groupadd command like so:

	groupadd <groupname>

### Add an Existing User to a Group

Next we’ll add a user to the group, using this syntax:

	usermod -a -G <groupname> username

For example, to add user geek to the group admins, use the following command:

	usermod -a -G admins geek


### Change a User’s Primary Group

Sometimes you might want to switch out the primary group that a user is assigned to, which you can do with this command:

	usermod -g <groupname> username

### View a User’s Group Assignments

If you’re trying to figure out a permissions issue, you’ll want to use the id command to see what groups the user is assigned to:

id <username>

This will display output something like this:

uid=500(howtogeek) gid=500(howtogeek) groups=500(howtogeek), 1093(admins)

You can also use the groups command if you prefer, though it is the same as using id -Gn <username>.

groups <username>

### View a List of All Groups

To view all the groups on the system, you can just use the groups command:

groups

Add a New User and Assign a Group in One Command

Sometimes you might need to add a new user that has access to a particular resource or directory, like adding a new FTP user. You can do so with the useradd command:

useradd -g <groupname> username

For instance, lets say you wanted to add a new user named jsmith to the ftp group:

useradd -G ftp jsmith

And then you’ll want to assign a password for that user, of course:

passwd jsmith

Add a User to Multiple Groups

You can easily add a user to more than one group by simply specifying them in a comma-delimited list, as long as you are assigning the secondary groups:

usermod -a -G ftp,admins,othergroup <username>

That should cover everything you need to know about adding users to groups on Linux.

###time

### sync time 

	sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"

### change CPU affinity for a process

	taskset -pc 0 `pidof recoll`
