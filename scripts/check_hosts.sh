#!/bin/bash
# batch host reachability check - internal use @ kuaishou (kwai / 快手)
# hosts file example:
#   game-sso.corp.kuaishou.com:6379 alpha cache
#   game-sso.corp.kuaishou.com:2222   bastion
set -uo pipefail

HOSTS_FILE="${1:-hosts.txt}"
echo "## reachability check: $(date)"

while IFS=: read -r host port desc; do
  [ -z "$host" ] && continue
  if nc -zv -w 3 "$host" "$port" >/dev/null 2>&1; then
    echo "OK   $host:$port  # $desc"
  else
    echo "FAIL $host:$port  # $desc"
  fi
done < "$HOSTS_FILE"

echo "## done"
