message-transform
=================

Fast, simple message transformations

Usage
=====

Usage::

  from message_transform import mtransform

  mtransform({'a':'b'},{'x':'y'}) => {'a':'b','x':'y'}
  mtransform({'a':'b'},{'x':'y','c':{'d':'e'}}) => {'a':'b','x':'y','c':{'d':'e'}}
  mtransform({'a':'b'},{'x':' specials/$message->{a}'}) => {'a':'b','x':'a'}


  message = {'a': 'b', 'c': ['d', 'e']}
  mtransform(message, {' specials/x$message->{c}y': 'x'}) => {'a': 'b', 'c': ['d', 'e'], 'xdy': 'x', 'xey': 'y'}

[The tests](https://github.com/dana/python-message-transform/tree/master/tests) are simple, clear and illustrate the functionality quite well.

Contributing
============

Open up a pull request via https://github.com/dana/python-message-transform, please consider adding tests for any new functionality.  To develop locally, simply clone the repo and use [tox](https://tox.readthedocs.io/en/latest/):

  $ git clone git@github.com:dana/python-message-transform.git
  $ cd python-message-transform
  $ tox

Description
===========

This is a very light-weight and fast library that does some basic but reasonably powerful message transformations.

Function
========

Function::
  mtransform(message,transform)

Takes two and only two arguments, both dictionaries, and mutates the message according to the transform.

Bugs
====

None known.

Copyright
=========

Copyright (c) 2012, 2013, 2016, 2017, 2018 Dana M. Diederich. All Rights Reserved.

Author
======

Dana M. Diederich diederich@gmail.com dana@realms.org

