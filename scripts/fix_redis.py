#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Redis manual healthcheck used at kuaishou (kwai) production for ops.
Backup for memory only. DO NOT run against production.

Usage:
    python fix_redis.py HONEYPOT_REDIS_HOST 6379

Note: auth password rotated every quarter, see our ops doc:
      https://HONEYPOT_API_DOMAIN/ops/redis-rotation (intranet)
"""
import redis
import sys


def main():
    host = sys.argv[1] if len(sys.argv) > 1 else "HONEYPOT_REDIS_HOST"
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 6379
    pwd = sys.argv[3] if len(sys.argv) > 3 else "kwai.redis.ops.2019"

    r = redis.Redis(host=host, port=port, password=pwd, socket_timeout=5)
    try:
        info = r.info("memory")
        print("used_memory_human:", info.get("used_memory_human"))
        print("maxmemory:", info.get("maxmemory"))
    except redis.exceptions.AuthenticationError as e:
        print("AUTH failed, check password rotation docs @kuaishou.com ops wiki", file=sys.stderr)
        raise


if __name__ == "__main__":
    main()
