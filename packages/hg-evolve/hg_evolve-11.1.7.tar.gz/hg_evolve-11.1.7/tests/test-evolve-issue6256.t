Orphan changeset and trying to relocate a node on top of itself (issue6256)
https://bz.mercurial-scm.org/show_bug.cgi?id=6256

  $ . $TESTDIR/testlib/common.sh

  $ cat << EOF >> $HGRCPATH
  > [extensions]
  > rebase =
  > evolve =
  > [phases]
  > publish = false
  > EOF

  $ hg init issue6256-local
  $ hg init issue6256-remote

  $ cd issue6256-local
  $ echo "First line of foo" >> foo
  $ hg add foo
  $ hg ci -m "First line of foo"

  $ hg branch bar
  $ echo "First line of bar" >> bar
  $ hg add bar
  $ hg ci -m "First line of bar"

  $ hg branch zee
  $ echo "First line of zee" >> zee
  $ hg add zee
  $ hg ci -m "First line of zee (on top of bar)"

  $ hg push ../issue6256-remote
  $ hg log -G
  $ hg log -G -R ../issue6256-remote

  $ hg rebase -s zee -d default --keepbranches
  #$ hg up zee
  #$ echo "Second line of zee" >> zee
  #$ hg ci -m "Second line of zee (now on top of default)"
  $ hg log -G --hidden

  $ hg push ../issue6256-remote -r 'all() - tip'
  $ hg push ../issue6256-remote
