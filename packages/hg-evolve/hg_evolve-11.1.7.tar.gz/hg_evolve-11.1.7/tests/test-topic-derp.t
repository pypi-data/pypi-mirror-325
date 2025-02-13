  $ . "$TESTDIR/testlib/topic_setup.sh"

  $ cat << EOF >> $HGRCPATH
  > [ui]
  > logtemplate = {rev} {branch} {get(namespaces, "topics")} {phase} {desc|firstline}\n
  > ssh = "$PYTHON" "$RUNTESTDIR/dummyssh"
  > [experimental]
  > tns-allow-rewrite = *
  > EOF

  $ cat << EOF >> $HGRCPATH
  > [server]
  > concurrent-push-mode = strict
  > EOF

  $ hg init main
  $ hg init draft
  $ cat << EOF >> draft/.hg/hgrc
  > [phases]
  > publish = no
  > EOF
  $ hg clone main client
  updating to branch default
  0 files updated, 0 files merged, 0 files removed, 0 files unresolved
  $ cat << EOF >> client/.hg/hgrc
  > [paths]
  > draft = ../draft
  > EOF


Testing core behavior to make sure we did not break anything
============================================================

Pushing a first changeset

  $ cd client
  $ echo aaa > aaa
  $ hg add aaa
  $ hg commit -m 'CA'
  $ hg outgoing -G
  comparing with $TESTTMP/main
  searching for changes
  @  0 default  draft CA
  
  $ hg push
  pushing to $TESTTMP/main
  searching for changes
  adding changesets
  adding manifests
  adding file changes
  added 1 changesets with 1 changes to 1 files

Pushing two heads

  $ echo aaa > bbb
  $ hg add bbb
  $ hg commit -m 'CB'
  $ echo aaa > ccc
  $ hg up 'desc(CA)'
  0 files updated, 0 files merged, 1 files removed, 0 files unresolved
  $ hg add ccc
  $ hg commit -m 'CC'
  created new head
  (consider using topic for lightweight branches. See 'hg help topic')
  $ hg outgoing -G
  comparing with $TESTTMP/main
  searching for changes
  @  2 default  draft CC
  
  o  1 default  draft CB
  
  $ hg push
  pushing to $TESTTMP/main
  searching for changes
  abort: push creates new remote head 9fe81b7f425d
  (merge or see 'hg help push' for details about pushing new heads)
  [20]
  $ hg outgoing -r 'desc(CB)' -G
  comparing with $TESTTMP/main
  searching for changes
  o  1 default  draft CB
  
  $ hg push -r 'desc(CB)'
  pushing to $TESTTMP/main
  searching for changes
  adding changesets
  adding manifests
  adding file changes
  added 1 changesets with 1 changes to 1 files

Pushing a new branch

  $ hg branch double//slash
  marked working directory as branch double//slash
  (branches are permanent and global, did you want a bookmark?)
  $ hg commit --amend
  $ hg outgoing -G
  comparing with $TESTTMP/main
  searching for changes
  @  3 double//slash  draft CC
  
  $ hg push
  pushing to $TESTTMP/main
  searching for changes
  abort: push creates new remote branches: double//slash//
  (use 'hg push --new-branch' to create new remote branches)
  [20]
  $ hg push --new-branch
  pushing to $TESTTMP/main
  searching for changes
  adding changesets
  adding manifests
  adding file changes
  added 1 changesets with 1 changes to 1 files (+1 heads)
  1 new obsolescence markers

Including on non-publishing

  $ hg push --new-branch draft
  pushing to $TESTTMP/draft
  searching for changes
  adding changesets
  adding manifests
  adding file changes
  added 3 changesets with 3 changes to 3 files (+1 heads)
  1 new obsolescence markers

Testing topic behavior
======================

Local peer tests
----------------

  $ hg up -r 'desc(CA)'
  0 files updated, 0 files merged, 1 files removed, 0 files unresolved
  $ hg topic babar
  marked working directory as topic: babar
  $ echo aaa > ddd
  $ hg add ddd
  $ hg commit -m 'CD'
  active topic 'default//babar' grew its first changeset
  (see 'hg help topics' for more information)
  $ hg log -G # keep track of phase because I saw some strange bug during developement
  @  4 default babar draft CD
  |
  | o  3 double//slash  public CC
  |/
  | o  1 default  public CB
  |/
  o  0 default  public CA
  

Pushing a new topic to a non publishing server should not be seen as a new head

  $ hg push draft
  pushing to $TESTTMP/draft
  searching for changes
  adding changesets
  adding manifests
  adding file changes
  added 1 changesets with 1 changes to 1 files (+1 heads)
  $ hg log -G
  @  4 default babar draft CD
  |
  | o  3 double//slash  public CC
  |/
  | o  1 default  public CB
  |/
  o  0 default  public CA
  
push --topic

  $ hg log -G -R $TESTTMP/draft
  o  3 default babar draft CD
  |
  | o  2 double//slash  public CC
  |/
  | o  1 default  public CB
  |/
  o  0 default  public CA
  
  $ echo bbb >> aaa
  $ hg commit -m "C'A"
  $ hg up 1
  2 files updated, 0 files merged, 1 files removed, 0 files unresolved
  $ hg topic --clear
  $ echo bbb >> bbb
  $ hg commit -m "C'B"
  $ hg log -G
  @  6 default  draft C'B
  |
  | o  5 default babar draft C'A
  | |
  | o  4 default babar draft CD
  | |
  | | o  3 double//slash  public CC
  | |/
  o |  1 default  public CB
  |/
  o  0 default  public CA
  
