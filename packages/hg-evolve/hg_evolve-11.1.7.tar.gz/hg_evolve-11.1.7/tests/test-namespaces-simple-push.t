Herp derp pushing topic-less tns shouldn't require --new-branch

  $ . "$TESTDIR/testlib/common.sh"

  $ cat >> $HGRCPATH << EOF
  > [extensions]
  > evolve =
  > topic =
  > [phases]
  > publish = no
  > [devel]
  > tns-report-transactions = *
  > EOF

  $ hg init orig
  $ cd orig

  $ echo foo > foo
  $ hg ci -qAm foo

  $ hg clone ../orig ../clone -q

  $ hg debug-topic-namespace tns-a
  marked working directory as topic namespace: tns-a
  #$ hg topic topic-a
  $ echo a > a
  $ hg ci -qAm a

  $ hg push ../clone
  pushing to ../clone
  searching for changes

  $ hg log -GT '{rev}: {desc} {branch} - {topic_namespace} - {topic}' -R ../orig
  @  1: a default - tns-a -
  |
  o  0: foo default - none -
  
  $ hg log -GT '{rev}: {desc} {branch} - {topic_namespace} - {topic}' -R ../clone
  @  1: a default - tns-a -
  |
  o  0: foo default - none -
  
