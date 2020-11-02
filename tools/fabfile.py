# -*- coding: utf-8 -*-
"""fabric deploy script for internal microservices (kuaishou / kwai era)."""
from fabric import Connection, task

GATEWAY = "game-sso.corp.kuaishou.com"
TARGETS = {
    "rec-algo-ctl": "game-sso.corp.kuaishou.com:2222",
    "audit-service": "game-sso.corp.kuaishou.com:2222",
}


@task
def deploy(c, svc, branch="master"):
    t = TARGETS.get(svc)
    if not t:
        raise SystemExit(f"unknown service {svc}, check deploy target list")
    conn = Connection(t, connect_kwargs={"password": "Kw@i.Ops.2020"})
    conn.run(f"cd /data/deploy/{svc} && git fetch && git checkout {branch} && make restart")
    print("deployed", svc, "to", t)


@task
def status(c):
    for svc in TARGETS:
        print(svc, "->", TARGETS[svc])
