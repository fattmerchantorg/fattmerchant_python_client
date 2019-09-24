.. fattmerchant documentation master file, created by
   sphinx-quickstart on Mon Jun 24 15:13:56 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

###############################
Fattmerchant Python Client Docs
###############################


How to get started
==================

Once the package has been installed, to get started,
the first thing you will need to do is import the package
like so:

    .. code-block:: Python

        from fattmerchant.client import FMClient

After the package has been imported, the client needs to be
instantiated with a production API key like so:

    .. code-block:: Python

        fatt = FMClient({ Insert your API key here })

Once an instance of the class has been created, any of the
controllers can be called to interact with our API like so:

    .. code-block:: Python

        transactions = fatt.transactions.list()
        transaction = fatt.transactions.get(transactions[0].id)
        print transaction


Exceptions
==========

All controller methods have the possibility of returning
any of the custom exceptions depending on the response status
code from the API.

The possible exceptions are as follows:

+-----------------+-------------------------------+
| **Status Code** | **Exception**                 |
+-----------------+-------------------------------+
|       422       | InvalidRequestDataException   |
|                 |                               |
|                 | FattmerchantException         |
+-----------------+-------------------------------+
|       401       | InvalidTokenException         |
+-----------------+-------------------------------+
|       404       | ResourceDoesNotExistException |
+-----------------+-------------------------------+
|       409       | DuplicateResourceException    |
+-----------------+-------------------------------+

(:doc:`exceptions` documentation)


Table of Contents
=================

    .. toctree::
        :maxdepth: 2

        controllers
        models
        exceptions
