
  $ . $TESTDIR/testlib/common.sh
  $ cat >> $HGRCPATH <<EOF
  > [phases]
  > publish = no
  > [extensions]
  > evolve =
  > topic =
  > hggit = /home/a/hg-features/hg-git/hggit
  > EOF

  $ hg version --verbose

  $ hg init orig
  $ hg clone orig clone

  $ cd clone
  $ mkcommit ROOT
  $ hg topic topic-a
  $ mkcommit A

Normal push with --debug

  $ hg push --debug
  pushing to $TESTTMP/orig
  query 1; heads
  searching for changes
  taking quick initial sample
  query 2; still undecided: 1, sample size is: 1
  2 total queries in 0.0188s
  listing keys for "phases"
  checking for updated bookmarks
  listing keys for "bookmarks"
  2 changesets found
  list of changesets:
  ea207398892eb49e06441f10dda2a731f0450f20
  b3f6025f72f66bec4dcd37a9084bb74a3ba31754
  bundle2-output-bundle: "HG20", 3 parts total
  bundle2-output-part: "replycaps" 227 bytes payload
  bundle2-output-part: "check:heads" streamed payload
  bundle2-output-part: "changegroup" (params: 1 mandatory) streamed payload
  bundle2-input-bundle: with-transaction
  bundle2-input-part: "replycaps" supported
  bundle2-input-part: total payload size 227
  bundle2-input-part: "check:heads" supported
  bundle2-input-part: total payload size 20
  bundle2-input-part: "changegroup" (params: 1 mandatory) supported
  adding changesets
  add changeset ea207398892e
  add changeset b3f6025f72f6
  adding manifests
  adding file changes
  adding A revisions
  adding ROOT revisions
  bundle2-input-part: total payload size 969
  bundle2-input-bundle: 3 parts total
  stable-range cache: unable to load, regenerating
  obshashrange cache: unable to load, regenerating
  updating the branch cache
  added 2 changesets with 2 changes to 2 files
  bundle2-output-bundle: "HG20", 1 parts total
  bundle2-output-part: "reply:changegroup" (advisory) (params: 0 advisory) empty payload
  bundle2-input-bundle: no-transaction
  bundle2-input-part: "reply:changegroup" (advisory) (params: 0 advisory) supported
  bundle2-input-bundle: 1 parts total
  listing keys for "phases"

  $ hg log -R ../orig -T '{rev}: {phase}\n'
  1: draft
  0: draft

  $ hg push --publish --config extensions.topic=! --debug
  pushing to $TESTTMP/orig
  query 1; heads
  searching for changes
  all remote heads known locally
  listing keys for "phases"
  checking for updated bookmarks
  listing keys for "bookmarks"
  no changes found
  bundle2-output-bundle: "HG20", 3 parts total
  bundle2-output-part: "replycaps" 227 bytes payload
  bundle2-output-part: "check:phases" 24 bytes payload
  bundle2-output-part: "phase-heads" 24 bytes payload
  bundle2-input-bundle: with-transaction
  bundle2-input-part: "replycaps" supported
  bundle2-input-part: total payload size 227
  bundle2-input-part: "check:phases" supported
  bundle2-input-part: total payload size 24
  bundle2-input-part: "phase-heads" supported
  bundle2-input-part: total payload size 24
  bundle2-input-bundle: 3 parts total
  bundle2-output-bundle: "HG20", 0 parts total
  bundle2-input-bundle: no-transaction
  bundle2-input-bundle: 0 parts total
  listing keys for "phases"
  [1]

  $ hg log -R ../orig -T '{rev}: {phase}\n'
  1: public
  0: public

  $ hg topic topic-b
  $ mkcommit B
  active topic 'topic-b' grew its first changeset
  (see 'hg help topics' for more information)

Nothing about hg-git in the caps...

  $ hg debugcapabilities ../orig
  Main capabilities:
    branchmap
    bundle2=HG20%0Abookmarks%0Achangegroup%3D01%2C02%2C03%0Acheckheads%3Drelated%0Adigests%3Dmd5%2Csha1%2Csha512%0Aerror%3Dabort%2Cunsupportedcontent%2Cpushraced%2Cpushkey%0Ahgtagsfnodes%0Alistkeys%0Aobsmarkers%3DV0%2CV1%0Aphases%3Dheads%0Apushkey%0Aremote-changegroup%3Dhttp%2Chttps%0Astream%3Dv2
    getbundle
    known
    lookup
    pushkey
    unbundle
  Bundle2 capabilities:
    HG20
    bookmarks
    changegroup
      01
      02
      03
    checkheads
      related
    digests
      md5
      sha1
      sha512
    error
      abort
      unsupportedcontent
      pushraced
      pushkey
    hgtagsfnodes
    listkeys
    obsmarkers
      V0
      V1
    phases
      heads
    pushkey
    remote-changegroup
      http
      https
    stream
      v2

  $ hg push --publish --debug --config extensions.aahggit=!
  pushing to $TESTTMP/orig
  query 1; heads
  searching for changes
  all remote heads known locally
  listing keys for "phases"
  checking for updated bookmarks
  listing keys for "bookmarks"
  listing keys for "namespaces"
  listing keys for "phases"
  listing keys for "bookmarks"
  1 changesets found
  list of changesets:
  65532fbb11d8373038670bdf740f8a7d2eba6220
  bundle2-output-bundle: "HG20", 5 parts total
  bundle2-output-part: "replycaps" 227 bytes payload
  bundle2-output-part: "check:phases" 24 bytes payload
  bundle2-output-part: "check:updated-heads" streamed payload
  bundle2-output-part: "changegroup" (params: 1 mandatory) streamed payload
  bundle2-output-part: "phase-heads" 24 bytes payload
  bundle2-input-bundle: with-transaction
  bundle2-input-part: "replycaps" supported
  bundle2-input-part: total payload size 227
  bundle2-input-part: "check:phases" supported
  bundle2-input-part: total payload size 24
  bundle2-input-part: "check:updated-heads" supported
  bundle2-input-part: total payload size 20
  bundle2-input-part: "changegroup" (params: 1 mandatory) supported
  adding changesets
  add changeset 65532fbb11d8
  adding manifests
  adding file changes
  adding B revisions
  bundle2-input-part: total payload size 492
  bundle2-input-part: "phase-heads" supported
  bundle2-input-part: total payload size 24
  bundle2-input-bundle: 5 parts total
  updating the branch cache
  added 1 changesets with 1 changes to 1 files
  bundle2-output-bundle: "HG20", 1 parts total
  bundle2-output-part: "reply:changegroup" (advisory) (params: 0 advisory) empty payload
  bundle2-input-bundle: no-transaction
  bundle2-input-part: "reply:changegroup" (advisory) (params: 0 advisory) supported
  bundle2-input-bundle: 1 parts total
  listing keys for "phases"

  $ hg log -R ../orig -T '{rev}: {phase}\n'
  2: public
  1: public
  0: public
