#require debhelper

  $ grep 'testedwith = ' "$TESTDIR"/../hgext3rd/evolve/metadata.py | \
  > grep -o "'([0-9.]+) "

Ensure debuild doesn't run the testsuite, as that could get silly.
  $ DEB_BUILD_OPTIONS=nocheck
  $ export DEB_BUILD_OPTIONS

  $ VERSION=`cd "$TESTDIR"/.. && python setup.py --version 2>/dev/null`
  $ mkdir ./mercurial-evolve_"$VERSION".orig
  $ cp -r "$TESTDIR"/../debian/ ./mercurial-evolve_"$VERSION".orig/
  $ cd ./mercurial-evolve_"$VERSION".orig/
  $ debuild -us -uc
  [1]

  $ cd ..
  $ hg archive -R "$TESTDIR"/.. evolve-archive
  $ cp "$TESTDIR"/../debian/changelog ./evolve-archive/debian/changelog
  $ cd evolve-archive
  $ head debian/changelog
  $ make deb-prepare > build.log 2>&1
  $ debuild -us -uc
