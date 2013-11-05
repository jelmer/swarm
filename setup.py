#!/usr/bin/python
# Setup file for dulwich
# Copyright (C) 2013 Jelmer Vernooij <jelmer@samba.org>

from distutils.core import setup

setup(name='swarm',
      description='Federated bug tracker',
      keywords='bugs distributed federated',
      version='0.0.1',
      url='http://samba.org/~jelmer/swarm',
      license='GPLv3 or later',
      author='Jelmer Vernooij',
      author_email='jelmer@samba.org',
      long_description="""A lightweight federated bug tracker.
      """,
      packages=['swarm'],
      scripts=['bin/swarm'],
      )
