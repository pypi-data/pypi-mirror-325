#!/bin/bash
past=${2:="6 months ago"}
datetime_past=$(date -d "$2" "+%Y-%m-%d %H:%M:%S")

git add .
GIT_COMMITTER_DATE=$datetime_past git commit --date="$datetime_past" -m "$1"

logs=$(git log --pretty=fuller)
echo "$logs"

# Usage:
# gitgod.sh "<commit_message>" "< <number> <days / months / years> ago>"
# gitgod.sh "testing h bhai" "1 month ago"