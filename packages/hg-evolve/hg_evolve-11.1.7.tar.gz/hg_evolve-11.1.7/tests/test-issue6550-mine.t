Amending s1 shouldn't take topic from s0 (issue6550)
https://bz.mercurial-scm.org/show_bug.cgi?id=6550

  $ . $TESTDIR/testlib/common.sh

  $ hg init issue6550
  $ cd issue6550
  $ cat > .hg/hgrc << EOF
  > [alias]
  > glog = log -GT "{rev}:{node|short} [{topic}] {desc}"
  > [extensions]
  > histedit =
  > evolve =
  > topic =
  > EOF

  $ hg topics foo
  marked working directory as topic: foo
  $ echo apple > a
  $ hg ci -qAm 'apple'
  $ hg topics --clear
  $ echo banana > a
  $ hg ci -m 'banana'

  $ hg glog
  @  1:ee789ae4ba85 [] banana
  |
  o  0:1519c60471a6 [foo] apple
  

  $ hg log --debug --hidden

  $ cat > editor.sh << 'EOF'
  > #!/bin/sh
  > echo message > "$1"
  > EOF

  $ HGEDITOR="sh ./editor.sh" hg histedit --rev . --commands - << EOF
  > mess ee789ae4ba85 1 banana
  > EOF

  $ hg glog
  @  2:6b89596d9703 [foo] message
  |
  o  0:1519c60471a6 [foo] apple
  

  $ hg debugobsolete
  ee789ae4ba85ac610b209749053d67b1844fd542 6b89596d9703586edd3d682e3a5e1f2f11b72eae 0 (Thu Jan 01 00:00:00 1970 +0000) {'ef1': '3', 'operation': 'histedit', 'user': 'test'}
  $ hg olog --all
  @  6b89596d9703 (2) message
  |    rewritten(description, meta) from ee789ae4ba85 using histedit by test (Thu Jan 01 00:00:00 1970 +0000)
  |
  x  ee789ae4ba85 (1) banana
  
