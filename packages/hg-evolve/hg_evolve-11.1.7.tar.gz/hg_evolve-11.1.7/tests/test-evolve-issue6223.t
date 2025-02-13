graft with evolve doesn't respect HGMERGE (issue6223)
https://bz.mercurial-scm.org/show_bug.cgi?id=6223

  $ . $TESTDIR/testlib/common.sh

  $ cat << EOF >> $HGRCPATH
  > [extensions]
  > evolve =
  > EOF

  $ hg init issue6223
  $ cd issue6223

  $ echo apricot > a
  $ hg ci -qAm apricot

  $ echo banana > b
  $ hg ci -qAm banana

  $ hg prune -r .
  #$ hg prev

  $ echo blueberry > b
  $ hg ci -qAm blueberry

  $ hg log -G --hidden

  $ export HGPLAIN=1
  $ export HGMERGE=:dump

  $ ls -l
  $ hg graft -r 1 --hidden
  $ ls -l
