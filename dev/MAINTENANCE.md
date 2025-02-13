# Maintenance

This document contains information about project governance and maintenance processes.

## Maintainers

The following individuals have generously donated their time to maintaining this project.

* Alex Stewart <alex.stewart@emerson.com> - Active. Lead Maintainer.
* Mark Silva <mark.silva@emerson.com> - Active. Cooperating Maintainer.

## Versioning Policy

This project uses [semantic versioning](https://semver.org/spec/v2.0.0.html), without release candidates. "Release" commits are tagged like `v${major}.${minor}`

## Release Process

This process should only be performed by a repo maintainer.

1. Create a PGP key associated with your identity.

1. Register your PGP key for use when signing tags.

   ``` bash
   gpg --list-keys \<$(git config --get user.email)\>  # Copy public key ID from output
   git config user.signingkey=$pubkey
   ```

1. Review PRs since the last release. Ensure that all notable changes are represented in the CHANGELOG.

   1. Commit any CHANGELOG updates.

1. Ensure the information in `conf.py` matches the releasing version.

   1. Commit any changes required.

1. Tag and sign the HEAD.

   ```bash
   git tag --sign v${major}.${minor}
   ```

1. Push the tag to github.

   ```bash
   git push origin v${major}.${minor}
   ```

1. Create a [new release](https://github.com/ni/nilrt-snac-guide/releases/new) in Github, attached to the tag you just pushed.

1. Inform the following people about the release and send a link to the release tag on the release page.

   * Steve Summers <steve.summers@emerson.com>
   * Evan Cone <evan.cone@emerson.com>
