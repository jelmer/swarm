swarm: A federated bug tracker
------------------------------

Terminology
===========

* bug report: a single report of a bug
* swarm: a bug report repository
* version: something that identifies a specific snapshot of the software; can
  be a version string ("1.0"), or a version control version
  ("add050707692f2f255b0a72d2d5175953af2920a")

Requirements
============

 * federated
  - but having a private clone shouldn't be necessary for day-to-day use
 * have an API (rest?)
 * web frontend
  - ordinary users should be able to report a bug without installing additional software
 * command-line UI
 * easily readable
 * restrict access to a single bug without making the rest inaccessible
 * granular access control; anonymous user may be able to create new bugs but not edit existing
 * ability to deal with bug 'graffiti' - spam or nuisance changes by users
 * users/developers can subscribe to bugs without needing a local swarm
 * able to close bugs from commit messages / NEWS files
 * slim
 * ability to do partial clones/imports
 * ability to track status in a different fork (a bug can be WONTFIX in upstream, but CONFIRMED in the fork)
 * ability to work with upstream/downstream and track their history of a bug

Each bug can have a list of versions that it is present in and versions that it is fixed in.

What it is not
--------------

 * A version control system
   ... but it should be able to talk to one
 * A release management system
   ... but it should be able to talk to one

It may be useful to get information about the revision/release graph
somewhere, but the bug tracker is not the primary location.

Possible future enhancements
----------------------------

 * email support

Per-bug metadata
~~~~~~~~~~~~~~~~

User identity is (like git) generally a name and an email address.

For each bug track:

 * Reporter identity
 * Bug title
 * Bug priority per stakeholder
 * Report date (inferred from history?)
 * List of subscribers
 * List of "versions" that it affects ("Found")
  - A version can be a revision SHA, a tarball name, etc.
  - Explicitly a list of versions rather than branches. If the versions
    are Git commit or Change-Ids then the revision graph can be used by
    the UI to see what branches are currently affected
 * List of Change-Ids/Revision-Ids in which it is known fixed ("NotFound")
 * List of tags
 * Related remote bugs and their status
 * History of all of the above
 * Comments

Implementation
==============

Storage
-------

Persistent
~~~~~~~~~~

Each bug is a separate ref in a git repository. Comments are stored in commit messages.
The commit has a tree object that contains a MANIFEST. Any additional files but
the bug MANIFEST that is added is considered an attachment.

Bugs are identified by a unique string; the SHA1 for the contents of
the original manifest.

Lookaside
~~~~~~~~~

There is an independent index kept along each swarm that is generated from the
persistent data. In some cases it may be possible to copy this index when cloning/fetching
from another swarm.

The index is used for searching, dupe detection and showing "Blocking" list of bugs
that are blocked by this bug.

MANIFEST Format
~~~~~~~~~~~~~~~
RFC822 headers:
* Version header
* Reporter (same format as git committer/author)
* Title
* Subscribers: List of mailto:user@example.com (or other URLs in the future)
* Assignee: List of assignees
* Versions: List of freeform text versions; e.g. git commit SHA, release version, full URL.
* Found: List of versions in which the bug was found
* NotFound: List of version in which the bug was missing
* Tags: List of tags
* Depends: List of bug ids
* Status

For per-branch bug reports or status, it's always possible to bring up a separate swarm or just mark other versions as affected.

Contents are the bug description

X- headers can be set and are ignored by swarm itself, but preserved. Other fields that it does
not know about cause warnings.

Using something like markdown or restructedText in the description might be useful; optional.

Refs, revision graph
~~~~~~~~~~~~~~~~~~~~

There will be one ref per bug, e.g. .git/refs/bugs/ae4f23.

A dupe merges the contents for the two bugs.  Once a dupe is marked, its ref
will point at the merged tree.

When pulling in a bug from a remote swarm into a local one, there are a couple
of options:

By default, all bugs which are not locally available are pulled in from a
remote. If there is divergence, nothing happens.  In some cases it might make
sense to merge the two branches. In other cases, just keep them separate and
let the user deal with it. Setting the ref to the zero sha can be used to block
further importing of the bug.  Behaviour could differ depending on what tags
are set; e.g. if 'upstream' is set on a debian branch, then that might be
reason to pull in a bug.

Like git remotes, remote refs are used for remote swarms.

E.g.:

.git/refs/remotes/samba/bugs/ae4f23
.git/refs/remotes/debian/bugs/e2341
.git/refs/remotes/ubuntu/bugs/e2341

Other random thoughts
=====================

Foreign bug tracking systems
----------------------------

It would be neat to support interoperability with other bug trackers,
distributed or otherwise. This shouldn't affect the complexity of the
core of the tracker; no extra abstraction layers, etc or a superset
of all data fields in foreign trackers. Perhaps a simple import/export
mechanism like fastimport/fastexport.

Independent repositories or data mixed into git repo
----------------------------------------------------

Data mixed in with the git code repository (not tree) rather than a separate
directory (.swarm/?) has advantages and disadvantages:

 + easy to pull in data with code
 + easier to debug/do ad hoc manipulation
 + easier to hook in various operations
 - more likely that git users break internal data/hit conflicts during pulls
 - noisier for git users (can be a lot of refs for e.g. samba)

It should be possible to support both modes, but we should not use this as an
excuse not to make a choice as it will make things slightly more complex for
users.

Bug nick names
--------------

By default bug reports are named based on the SHA1 of their initial MANIFEST.
There is nothing stopping the use of arbitrary strings to be used as bug
names.

How would collisions be handled in this case? Perhaps just have symrefs for
bug nick names and always keep the SHA1 version?

Open Questions
==============

* A user report is not the same thing as a bug report. Okay if they just file
  bug reports that later get merged? What about PII in user reports?
  - Having a separate object kind for user reports just adds more noise and
    complexity - both in the code and in the UI - so let's just use generic bug
    reports for these
  - Perhaps have a way of creating bug reports that are referenced when
    deduping but not a part of the DAG, so they can be obliterated without
    breaking the DAG.
* Should a bug have a list of branches it affects? Are versions enough?
* How to e.g. track multiple debian packages in a single swarm,
  or having a single local swarm to track all my bugs in a lot of
  different upstreams?
 - would want to be able to push (as opposed to pull) all local changes upstream
   + perhaps with some exceptions?
 - would want to 'rebase'/merge local comments in some cases (e.g. offline use)
