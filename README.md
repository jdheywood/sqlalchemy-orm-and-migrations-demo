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

Then assume the demo user and activate the python virtual environment (note the hyphen, this is needed to activate the python venv)

```
sudo su - demo
```

Execute the existing database schema migrations to create tables in your new db

```
cd code
alembic -n demo upgrade head
```

And then run the tests to see the ORM in action

```
nosetests
```

##### Further steps
Create a new model and generate a migration

```
TODO
```

Run the migration against your database

```
TODO
```

You should see the new table ready for use, inspect either via psql in the VM or using your SQL client of choice (PSequel is a simple to use free tool)

Remove your table by migrating downwards one step in the version history

```
TODO
```

Review the head of the migration versions via this command

```
TODO
```

Further reading on alembic can be found here (Alembic)[www.alembic.com.probably]


