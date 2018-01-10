# ORM and Data Migration Demo
##### A Short Brighton Python Talk
This repo consists of the presentation & codebase demonstated at Brighton Python

### Running the code
##### Setup
1. Clone this repo
2. Download & install [Vagrant](https://www.vagrantup.com/).

Open a Terminal and navigate to the checked out folder.
```
vagrant up
```

Once the VM is up and running ssh in via;

```
vagrant ssh
```

This will automatically assume the vagrant user and activate the python virtual environment courtesy of the demo_bash_profile copied over during provsioning.

Now you can connect to the postgres database using the following command.

```
psql -d demo
```

You'll be prompted for the password, as you can see in provision.yml this is 'vagrant', so type that in and you are away. 

When you have had a look around exit via \q


To execute the existing database schema migrations (& create tables in your new db) you'll need to run the following commands.

```
cd host/code
alembic -n demo upgrade head
```

Now you have a schema you'll need some data, so run the add_materials script

```
PYTHONPATH=/home/vagrant/host/code python -m scripts.add_materials
```

This script uses the ORM to create data. Have a read through it to familiarise yourself with the main concepts; connection, engine, session, add & commit.

Whilst we're discussing scripts, we also have a remove_materials script that, yep you've guessed it, removes the materials data. Should you wish to run this; 

```
PYTHONPATH=/home/vagrant/host/code python -m scripts.remove_materials
```


Once you have some data you can run the tests which demonstrate some more uses of the ORM via the command;

```
nosetests -v
```

### Connecting to the demo database from your host machine

For connecting to the postgres demo database from a client on your host machine you'll need the following details (note that you can always find these in Vagrantfile and provision.yml);

```
Host: localhost
Port: 5433
User: vagrant
Password: vagrant
Database: demo
```

Note that I've re-mapped the default port 5432 to 5433 in order to prevent conflicts with other postgres databases you may have running, you can change this in the Vagrantfile if you so wish. If you do you'll need to re-provision, so exit the VM and run the commend below to apply your changes.

```
vagrant provision
```



### Further steps
Create a new model and generate a migration

```
/* your new model code here, follow the examples in this repo if you are unsure */

alembic -n development revision -m "Some meaningful description of the changes" --autogenerate
```

Run the migration against your database

```
alembic -n development upgrade head
```

You should see the new table ready for use, inspect either via psql in the VM or using your SQL client of choice (PSequel is a simple to use free tool).

Remove your table by migrating downwards one step in the version history

```
alembic -n development downgrade -1
```

Review the current head of your database the migration versions via this command

```
alembic -n development heads
```

Review the version history of the versions

```
alembic -n development history
```


Further reading on alembic can be found here (Alembic)[http://alembic.zzzcomputing.com/en/latest/]


