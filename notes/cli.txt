Command-line interface
----------------------

The 'bts' utility from Debian works quite well - perhaps model it after that?

    show [<options>] [<bug number> | <package> | <maintainer> | : ] [<opt>=<val> ...]

    show [<options>] [src:<package> | from:<submitter>] [<opt>=<val> ...]

    show [<options>] [tag:<tag> | usertag:<tag> ] [<opt>=<val> ...]

    show [release-critical | release-critical/... | RC]

    bugs [<options>] [<bug_number> | <package> | <maintainer> | : ] [<opt>=<val> ...]

    bugs [<options>] [src:<package> | from:<submitter>] [<opt>=<val> ...]

    bugs [<options>] [tag:<tag> | usertag:<tag> ] [<opt>=<val> ...]

    bugs [release-critical | release-critical/... | RC]

    select [<key>:<value> ...]

    status [<bug> | file:<file> | fields:<field>[,<field> ...] | verbose] ...

    clone <bug> <new_ID> [<new_ID> ...]

    done <bug> [<version>]

    reopen <bug> [<submitter>]

    archive <bug>

    unarchive <bug>

    retitle <bug> <title>

    summary <bug> [<messagenum>]

    submitter <bug> [<bug> ...] <submitter-email>

    reassign <bug> [<bug> ...] <package> [<version>]

    found <bug> [<version>]

    notfound <bug> <version>

    fixed <bug> <version>

    notfixed <bug> <version>

    block <bug> by|with <bug> [<bug> ...]

    unblock <bug> by|with <bug> [<bug> ...]

    merge <bug> <bug> [<bug> ...]

    forcemerge <bug> <bug> [<bug> ...]

    unmerge <bug>

    tag <bug> [+|-|=] <tag> [<tag> ...]

    tags <bug> [+|-|=] <tag> [<tag> ...]

    affects <bug> [+|-|=] <package> [<package> ...]

    user <email>

    usertag <bug> [+|-|=] <tag> [<tag> ...]

    usertags <bug> [+|-|=] <tag> [<tag> ...]

    claim <bug> [<claim>]

    unclaim <bug> [<claim>]

    severity <bug> <severity>

    forwarded <bug> <address>

    notforwarded <bug>

    package [<package> ...]

    limit [<key>[:<value>]] ...

    owner <bug> <owner-email>

    noowner <bug>

    subscribe <bug> [<email>]

    unsubscribe <bug> [<email>]

    reportspam <bug> ...

    spamreport <bug> ...

    cache [<options>] [<maint_email> | <pkg> | src:<pkg> | from:<submitter>]

    cache [<options>] [release-critical | release-critical/... | RC]

    cleancache <package> | src:<package> | <maintainer>

    cleancache from:<submitter> | tag:<tag> | usertag:<tag> | <number> | ALL

    version
