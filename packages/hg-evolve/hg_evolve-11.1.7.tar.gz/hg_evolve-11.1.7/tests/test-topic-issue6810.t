Pushing and publishing a recently amended changeset without --force (issue6810)
https://bz.mercurial-scm.org/show_bug.cgi?id=6810

  $ . "$TESTDIR/testlib/topic_setup.sh"
  $ . "$TESTDIR/testlib/common.sh"

  $ cat << EOF >> "$HGRCPATH"
  > [phases]
  > publish = no
  > EOF

  $ hg init issue6810-server
  $ hg clone issue6810-server issue6810-client

  $ cd issue6810-client
  $ mkcommit ROOT
  $ hg phase --public -r 'all()'
  #$ hg topic antelope
  $ mkcommit A0
  $ hg push

topic prepared, now the interesting part

  $ mkcommit B0
  $ hg push

immediately creating a successor of B0

  $ hg commit --amend -m B1

  $ hg log -G --hidden -T '{rev}: {desc} ({topic}) ({phase})\n' -R ../issue6810-server
  $ hg log -G --hidden -T '{rev}: {desc} ({topic}) ({phase})\n'

server doesn't have B0 nor B1, now let's push and publish at the same time

  $ hg push -r . --publish
  new [b'3fca038f07ad', b'ea207398892e']
  nowarn []
  old [b'ea207398892e']
  diff [b'3fca038f07ad']

  $ hg push -r .

  $ hg log -G --hidden -T '{rev}:{node|short} {desc} ({topic}) ({phase})\n' -R ../issue6810-server
  $ hg log -G --hidden -T '{rev}:{node|short} {desc} ({topic}) ({phase})\n'

  $ cd ..
