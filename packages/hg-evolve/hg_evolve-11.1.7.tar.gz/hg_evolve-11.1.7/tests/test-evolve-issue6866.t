TODO (issue6866)
https://bz.mercurial-scm.org/show_bug.cgi?id=6866

  $ . $TESTDIR/testlib/common.sh

  $ cat << EOF >> $HGRCPATH
  > [phases]
  > publish = no
  > [extensions]
  > rebase =
  > evolve =
  > EOF

  $ hg init orig
  $ hg clone orig clone
  updating to branch default
  0 files updated, 0 files merged, 0 files removed, 0 files unresolved
  $ cd clone

  $ mkcommit ROOT
  $ hg push
  pushing to $TESTTMP/orig
  searching for changes
  adding changesets
  adding manifests
  adding file changes
  added 1 changesets with 1 changes to 1 files

  $ hg branch branch-a
  marked working directory as branch branch-a
  (branches are permanent and global, did you want a bookmark?)

  $ echo apricot > a
  $ hg ci -qAm apricot

  $ hg push --new-branch

  $ hg branch branch-a-amend
  $ hg ci --amend

  $ hg branch branch-b
  marked working directory as branch branch-b

  $ echo banana > b
  $ hg ci -qAm banana

  $ hg branch branch-b-amend
  $ hg amend

  $ hg push --new-branch
