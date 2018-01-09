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

Once the VM is up and running ssh in via

```
vagrant ssh
```

This will automatically assume the vagrant user and activate the python virtual environment courtesy of the demo_bash_profile copied over during provsioning

Now you can connect to the postgres database using the following command

```
psql -d demo
```

You'll be prompted for the password, as you can see in provision.yml this is 'vagrant', so type that in and you are away.



Execute the existing database schema migrations to create tables in your new db

```
cd code
alembic -n demo upgrade head
```

And then run the tests to see the ORM in action

```
nosetests
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

Note that I've re-mapped the default port 5432 to prevent conflicts with other postgres databases you may have running, you can change this in the Vagrantfile if you so wish.




### Further steps
Create a new model and generate a migration

```
TODO
```

Run the migration against your database

```
TODO
```

You should see the new table ready for use, inspect either via psql in the VM or using your SQL client of choice (PSequel is a simple to use free tool).

Remove your table by migrating downwards one step in the version history

```
TODO
```

Review the head of the migration versions via this command

```
TODO
```

Further reading on alembic can be found here (Alembic)[www.alembic.com.probably]


