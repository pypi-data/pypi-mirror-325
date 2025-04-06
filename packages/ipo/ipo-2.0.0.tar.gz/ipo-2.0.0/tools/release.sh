#!/bin/bash

# © 2020, Midgard
# License: GPL-3.0-or-later
# This file is not available under the LGPL!

set -e

cd $(dirname "$0")/..

if [ ! -t 0 ] ; then
	echo "release.sh should be run with a terminal attached to stdin" >&2
	exit 1
fi

tools/test.sh

source venv3.11/bin/activate
pip install twine

git status

echo -n "Previous version:  v"
prev_version="$(./setup.py --version)"
echo "$prev_version"
read -p "Enter new version: v" version

tagid=v"$version"
if [ "$version" != "$prev_version" ]; then
	sed -i 's/version=".*"/version="'"$version"'"/' setup.py
	sed -i 's/## \[Unreleased\]/&\n### Added\n### Changed\n### Deprecated\n### Removed\n### Fixed\n### Security\n\n## ['"$version"'] - '"$(date --utc +%Y-%m-%d)"'/' CHANGELOG.md
	echo; echo "Inspect CHANGELOG..."
	${EDITOR:-nano} CHANGELOG.md
	git add setup.py CHANGELOG.md
	git commit -m "Bump version to $version"

	echo "Creating git tag $tagid"
	git tag -s -m "Version $version" "$tagid"
else
	echo "Version already created; building wheel and uploading"
fi

./setup.py sdist bdist_wheel

read -p "Upload to Git and PyPI? (y/N) " confirm
if [ ! "$confirm" = y ]; then "Abort"; exit 1; fi

python3 -m twine upload dist/*-${version}*
git push origin "$tagid" master
