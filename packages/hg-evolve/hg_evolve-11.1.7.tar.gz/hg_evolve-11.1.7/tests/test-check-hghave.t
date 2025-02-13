#require test-repo

  $ . "$RUNTESTDIR/helpers-testrepo.sh"

  $ cd "$TESTDIR"/..

Checking all non-public revisions on all compatibility branches up to the
current commit

  $ for node in `testrepohg log --rev 'branch("re:^mercurial-") and ::. and not public() and not desc("# no-check-commit")' --template '{node|short}\n'`; do
  >   testrepohg grep --rev $node ' \([^)]*hg[0-9]+[^!)]* !\)' tests/*.t
  >   testrepohg grep --rev $node '^#(if|require) .*hg[0-9]+' tests/*.t
  > done
