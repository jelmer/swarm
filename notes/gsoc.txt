distributed bugtrackers


op: has anyone used them before?
:(- what are they?)
:LWN article a while back
:basic support in some trackers, but nonstandardised

fossil
:wiki, bugtracker

webif important for the user
:existing don't generally supply this

noise in SCM
:could just use a separate git, but that loses association

joomla -> test system for applying/unapplying bugfixes

launchpad bugtracker a common source of ennui, not capable enough
github allows pulling, but needs project API key
no "pull request" for issues
(same thing for distros when people report issues against distro that is really an issue against upstream)

convergence of bugs to upstream?  or even browsing through branches

plugins that act on commit text "fixes #3" break when you pull to git fork with independent bug tracker, need unique bug IDs

taskwarrior -> bugwarrior syncer
debian also walks bugs & tries to grab upstream status automatically from ref

no one actually using distributed bugtracker

minimum reqs:
* forkable - get bugs with the code
* full database of bugs doesn't seem required, but should be possible
* web UI
* low interference with VCS desired

location of bugs? in tree? branch? (split opinions...)
mapping between issues and branches

handling of large bugs/attachments

noise (esp. merges) is really a UX problem

bugs are valuable at a central location

conflict behaviour?
same problem as with central bugtrackers, window just larger

issues specific to bugs but not code?
* UI
* assigning bugs to people
* bugmails

distbugs.branchable.com? (derelict)
syncwith.us defects / sd / "prophet" (dist DB, perl)

dumping & forking classic bugtracker relatively easy... merging not so much

centralised bugtracker with clonability & queuing calls
also: test-driven bugtracking :)

google code hosting discontinued API
