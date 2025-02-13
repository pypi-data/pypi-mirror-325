** Testing resolution of orphans by `hg evolve` when merges are involved **

  $ . $TESTDIR/testlib/common.sh

  $ cat >> $HGRCPATH <<EOF
  > [ui]
  > interactive = True
  > [extensions]
  > evolve =
  > EOF

Repo Setup

  $ hg init repo
  $ cd repo
  $ echo ".*\.orig" > .hgignore
  $ hg add .hgignore
  $ hg ci -m "added hgignore"

An orphan merge changeset with one of the parent obsoleted
==========================================================

1) When merging both the parents does not result in conflicts
-------------------------------------------------------------

  $ echo foo > a
  $ hg ci -Aqm "added a"
  $ hg up .^
  0 files updated, 0 files merged, 1 files removed, 0 files unresolved
  $ echo foo > b
  $ hg ci -Aqm "added b"
  $ hg up c7586e2a9264
  1 files updated, 0 files merged, 1 files removed, 0 files unresolved
  $ hg merge
  1 files updated, 0 files merged, 0 files removed, 0 files unresolved
  (branch merge, don't forget to commit)
  $ hg ci -m "merging a and b"

  $ hg glog
  @    3:3b2b6f4652ee merging a and b
  |\    () draft
  | o  2:d76850646258 added b
  | |   () draft
  o |  1:c7586e2a9264 added a
  |/    () draft
  o  0:8fa14d15e168 added hgignore
      () draft

Checking issue6141 while at it: p1 is 1 and p2 is 2

  $ hg parents
  changeset:   3:3b2b6f4652ee
  tag:         tip
  parent:      1:c7586e2a9264
  parent:      2:d76850646258
  user:        test
  date:        Thu Jan 01 00:00:00 1970 +0000
  summary:     merging a and b
  

Testing with obsoleting the second parent

  $ hg up d76850646258
  0 files updated, 0 files merged, 1 files removed, 0 files unresolved
  $ echo bar > b
  $ hg amend
  1 new orphan changesets

  $ hg glog
  @  4:64370c9805e7 added b
  |   () draft
  | *    3:3b2b6f4652ee merging a and b
  | |\    () draft
  +---x  2:d76850646258 added b
  | |     () draft
  | o  1:c7586e2a9264 added a
  |/    () draft
  o  0:8fa14d15e168 added hgignore
      () draft

  $ hg evolve --all --update
  move:[3] merging a and b
  atop:[4] added b
  working directory is now at 91fd62122a4b

  $ hg glog
  @    5:91fd62122a4b merging a and b
  |\    () draft
  | o  4:64370c9805e7 added b
  | |   () draft
  o |  1:c7586e2a9264 added a
  |/    () draft
  o  0:8fa14d15e168 added hgignore
      () draft

Following issue6141: FIXME: p2 is now 1

  $ hg parents
  changeset:   5:91fd62122a4b
  tag:         tip
  parent:      4:64370c9805e7
  parent:      1:c7586e2a9264
  user:        test
  date:        Thu Jan 01 00:00:00 1970 +0000
  summary:     merging a and b
  

  $ hg files -r 3 --hidden
  .hgignore
  a
  b
  $ hg files -r 5 --hidden
  .hgignore
  a
  b

  $ hg diff -r 3 -r 5 --hidden
  diff -r 3b2b6f4652ee -r 91fd62122a4b b
  --- a/b	Thu Jan 01 00:00:00 1970 +0000
  +++ b/b	Thu Jan 01 00:00:00 1970 +0000
  @@ -1,1 +1,1 @@
  -foo
  +bar
