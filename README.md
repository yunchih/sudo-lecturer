# Sudo lecturer

## Motivation

Instead of lecturing users by `sudo`'s default lecture message:
```

We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

    #1) Respect the privacy of others.
    #2) Think before you type.
    #3) With great power comes great responsibility.
```

and threating them after they have futilely typed their password:

```
[username] is not in the sudoers file. This incident will be reported.
```

It is better to prevent the users from even trying and show them
a friendly warning for education purpose, by setting the following
in `/etc/sudoers`:


```
Defaults lecture = always
Defaults lecture_file = /etc/sudo-lectures.txt
Defaults passwd_tries = 0
```

Such approach can be extended further to display different
messages each time a `sudo` attempt is performed.  Our Python
script uses `inotify` to monitor `lecture_file` and alter its
content whenever it is opened and displayed to some users.

## Usage

The script `sudo-daemon` will read the filepath of `lecture_file`
via an environment variable: `SUDO_LECTURE_FILE`.

``` bash
python setup.py install
export SUDO_LECTURE_FILE=/etc/sudo-lectures.txt
sudo-daemon
```
