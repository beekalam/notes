### remap caps lock to ctrl

To permanently change the behaviour:

    run dconf-editor

    select org.gnome.desktop.input-sources

    Change xkb-options to ['ctrl:nocaps'] (or add it to any existing options)

or on the command line (Warning -- this overwrites your existing settings!):

gsettings set org.gnome.desktop.input-sources xkb-options "['ctrl:nocaps']"

### how teo tell which version of library you have?

	$ dpkg -l '*ssh*'




