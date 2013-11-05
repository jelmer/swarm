#!/usr/bin/python -u
#
# swarm - a federated bug tracker
# Copyright (C) 2013 Jelmer Vernooij <jelmer@samba.org>
# vim: expandtab
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; version 3
# or (at your option) a later version of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA  02110-1301, USA.

"""A federated bug tracker."""

__version__ = (0, 0, 1)


class BugReport(object):
    """A bug report."""


class BugManifest(object):
    """Manifest for a bug report.

    """


class Swarm(object):
    """A collection of bug reports.

    :ivar repo: `dulwich.repo.Repo` instance used for storage.
    """

    def __init__(self, repo):
        """Open a swarm from a Git repo.

        :param repo: A `dulwich.repo.Repo` instance
        """
        self.repo = repo

    @classmethod
    def from_path(cls, path):
        from dulwich.repo import Repo
        r = Repo(path)
        return cls(r)
