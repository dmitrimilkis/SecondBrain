#!/usr/bin/env bash
# Rebuild tools/books/ from the exact Standard Ebooks source commits used on 2026-09-29.
set -euo pipefail
cd "$(dirname "$0")"
export GIT_LFS_SKIP_SMUDGE=1
mkdir -p books .src
tail -n +2 sources.tsv | while IFS=$'\t' read -r key repo commit; do
  dir=".src/$repo"
  if [ ! -d "$dir/.git" ]; then
    git init -q "$dir"
    git -C "$dir" remote add origin "https://github.com/standardebooks/$repo"
  fi
  git -C "$dir" fetch -q --depth 1 origin "$commit"
  git -C "$dir" checkout -q FETCH_HEAD
  python3 extract.py "$dir" "books/$key.txt"
done
