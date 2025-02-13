Limiting topic namespaces during exchange based on a config option

  $ . "$TESTDIR/testlib/common.sh"

  $ cat >> $HGRCPATH << EOF
  > [extensions]
  > topic =
  > [phases]
  > publish = no
  > [ui]
  > ssh = "$PYTHON" "$RUNTESTDIR/dummyssh"
  > EOF

  $ hg init repo
  $ cd repo

  $ mkcommit ROOT
  $ hg phase -r . --public
  $ echo foo > foo
  $ hg topic topic-foo
  marked working directory as topic: topic-foo
  $ hg ci -qAm foo

  $ cd ..

  $ hg clone repo visible
  updating to branch default
  1 files updated, 0 files merged, 0 files removed, 0 files unresolved
  $ cat >> visible/.hg/hgrc << EOF
  > [server]
  > view = visible
  > EOF

  $ hg clone repo immutable
  updating to branch default
  1 files updated, 0 files merged, 0 files removed, 0 files unresolved
  $ cat >> immutable/.hg/hgrc << EOF
  > [server]
  > view = immutable
  > [phases]
  > publish = yes
  > EOF

  $ hg clone ssh://user@dummy/visible wip -q
  $ cd wip

  $ hg log -GT '{rev}: {desc} {fqbn} ({phase})' -R ../repo
  $ hg log -GT '{rev}: {desc} {fqbn} ({phase})' -R ../visible
  $ hg log -GT '{rev}: {desc} {fqbn} ({phase})' -R ../immutable
  $ hg log -GT '{rev}: {desc} {fqbn} ({phase})' -R ../wip

  $ grep topic-foo ../repo/.hg/cache/* | sort
  $ grep topic-foo ../visible/.hg/cache/* | sort
  $ grep topic-foo ../immutable/.hg/cache/* | sort
  $ grep topic-foo ../wip/.hg/cache/* | sort

  #$ rm ../wip/.hg/cache/rbc*

  $ hg push -r tip ssh://user@dummy/immutable
  pushing to ssh://user@dummy/immutable
  searching for changes
  remote: adding changesets
  remote: adding manifests
  remote: adding file changes
  remote: added 0 changesets with 0 changes to 1 files

  $ cd ..
