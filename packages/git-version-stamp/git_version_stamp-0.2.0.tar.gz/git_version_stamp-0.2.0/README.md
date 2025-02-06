# git-version-stamp

This small utility (written in Python) creates a simple version code based
on the status of a git repo/tree for files of interest, mostly for use in
build scripts to embed into build output and/or name build artifacts.

You should also consider these more established tools:
- [dunamai](https://github.com/mtkennerly/dunamai#readme)
- [git describe](https://git-scm.com/docs/git-describe)
- [setuptools-git-versioning](https://setuptools-git-versioning.readthedocs.io/)
- [setuptools-scm](https://github.com/pypa/setuptools-scm#readme)
- [versioneer](https://github.com/python-versioneer/python-versioneer#readme)
- [versioningit](https://versioningit.readthedocs.io/)

The main differences with this one:
- In general it's much less developed than any of those
- It doesn't integrate with setuptools, it just spits out a version string
- It uses timestamp-oriented versioning (rather than last-tag-plus-change-count)
  for untagged builds, which is more useful for apps or firmware images
  but less appropriate for libraries
- It lets you pick a subset of files in the repo via include and exclude
  lists, and the version is based on the status of those files

This utility can be run as a script (`git-version-stamp`) or imported as a
library (`import git_version_stamp`). Look at the source for usage, it's
quite trivial.

If you actually use this, maybe let me (egnor@ofb.net) know so I'm a bit
more motivated to make it a proper project with docs and tests and stuff?
PRs welcome in any case.
