# Settings quoted on the page

Short excerpts of the launcher and the window's settings as installed in October 2026, with folder names replaced.
The 12 October trace script is in `records/2026-10-12_engine-trace/`.
The window app's own source is not published; these are only the lines a reader needs to reproduce the setup.

## Engine environment (every home)

The window copies only these variables from its own environment when they are set: `PATH`, `HOME`, `LANG`, `LC_*`,
`USER`, `LOGNAME`, `SHELL` (a real shell only), `XDG_RUNTIME_DIR`, `TMPDIR`, `LETTA_LOCAL_BACKEND_DIR`, `LETTA_CLI_PATH`,
`LLAMA_CPP_BASE_URL`, `LLAMACPP_BASE_URL`, `OLLAMA_BASE_URL`, `LMSTUDIO_BASE_URL`, and the engine's local-service
waiting times (whole milliseconds, up to two hours). Then it forces, last, so they always win:

```
LETTA_CODE_TELEM=0
DO_NOT_TRACK=1
DISABLE_AUTOUPDATER=1
LETTA_CODE_OFFLINE=1
LETTA_DISABLE_LSP_DOWNLOAD=1
LETTA_DISABLE_MODS=1
LETTA_DISABLE_CRON_SCHEDULER=1
LETTA_BASE_URL=http://127.0.0.1:9
```

The six privacy switches were tested only as a group (12 October). `LETTA_BASE_URL` covers requests that use the
engine's Letta API address; in the window's source comment, telemetry and feedback ignore it and are stopped by
`LETTA_CODE_TELEM` and `DO_NOT_TRACK`.

In a sealed window, a model address in any of the four model variables that is not `127.0.0.1`, `localhost` or `::1`
stops the engine from starting, with a plain sentence.

The engine is started as:

```
<electron> <engine>/letta.js --backend local server --listen ws://127.0.0.1:0 --ws-auth capability-token --ws-token-sha256 <hash>
```

Before every start the window adds these to `permissions.deny` in the home's `.letta/settings.json`:
`Wake`, `Monitor`, `WatchPR`, `Workflow`, `SendAgentMessage`, `Task`, `Agent`.

## The 12 October trace (engine alone)

`records/2026-10-12_engine-trace/run-engine-traced.sh` is the script used. With `switches` it sets the first six
variables above (and `LETTA_LOCAL_BACKEND_DIR`); with `factory` it sets none. It runs
`strace -f -qq -e trace=connect,sendto,sendmmsg -s 300` around `node letta.js --backend local`.

## Sandbox (sealed home; the connected home drops `--unshare-net` and adds the three binds noted below)

This is the command shape with folder names replaced. It is an excerpt: the launcher also sets, inside, the config
folder, a permission ceiling (`standard`), background commands off and the confinement mode (`launcher`), and it
needs an unprivileged `bwrap` and the folders named here to exist.

```
bwrap --unshare-user --unshare-ipc --unshare-uts --unshare-cgroup --unshare-pid --unshare-net \
  --die-with-parent --new-session --clearenv --cap-drop ALL \
  --ro-bind /usr /usr --symlink usr/bin /bin --symlink usr/sbin /sbin --symlink usr/lib /lib --symlink usr/lib64 /lib64 \
  --dir /etc --ro-bind <gate>/etc/passwd /etc/passwd --ro-bind <gate>/etc/group /etc/group \
  --ro-bind <gate>/etc/hosts /etc/hosts \
  --ro-bind /etc/nsswitch.conf /etc/nsswitch.conf --ro-bind /etc/ld.so.cache /etc/ld.so.cache \
  --ro-bind /etc/fonts /etc/fonts --ro-bind /etc/localtime /etc/localtime \
  --proc /proc --size 1073741824 --tmpfs /tmp \
  --tmpfs /dev --dev-bind /dev/null /dev/null --dev-bind /dev/zero /dev/zero --dev-bind /dev/urandom /dev/urandom \
  --dev-bind /dev/dri /dev/dri --perms 1777 --size 536870912 --tmpfs /dev/shm \
  --dir /home --bind <this home> /home/<user> \
  --bind <window settings for this home> /winconf \
  --ro-bind <window build> /app \
  --ro-bind <engine 0.34.10> /engine \
  --ro-bind <gate> /gate \
  --ro-bind <node> /node --ro-bind <model door folder> /door \
  --perms 0700 --dir /run/user/1000 --ro-bind <wayland socket> /run/user/1000/wayland-0 \
  --chdir /home/<user> \
  --setenv HOME /home/<user> --setenv LANG C.UTF-8 --setenv SHELL /bin/bash --setenv PATH /usr/bin:/bin \
  --setenv XDG_RUNTIME_DIR /run/user/1000 --setenv WAYLAND_DISPLAY wayland-0 --setenv XDG_SESSION_TYPE wayland \
  --setenv LETTA_WINDOW_MODE sealed \
  --setenv LETTA_CLI_PATH /engine/node_modules/@letta-ai/letta-code/letta.js \
  --setenv LLAMA_CPP_BASE_URL http://127.0.0.1:<relay port>/v1 \
  /bin/bash /gate/inner.sh
```

Connected only: `--ro-bind /etc/resolv.conf /etc/resolv.conf --ro-bind /etc/ssl /etc/ssl --ro-bind /etc/ca-certificates /etc/ca-certificates`.
Sealed only, when installed: read-only binds for the lend, API, speech and robot doors' socket folders.

`<gate>/etc/hosts` always begins with:

```
127.0.0.1 localhost
::1 localhost
```

In the connected home it then lists each name in `records/settings/blocked-hosts.txt` twice, as `0.0.0.0 <name>` and
`:: <name>`. The launcher refuses to open if fewer than seven names are written or `letta.com` or `api.letta.com` is missing.

Inside, `inner.sh` starts the relay (`node --disable-sigusr1 model-relay.cjs`, a loopback port joined to `/door/model.sock`)
and then the window: `electron /app --no-sandbox --ozone-platform=wayland --password-store=basic`.

## Window page and Chromium

Content policy on the page:

```
default-src 'self'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; font-src 'self'; script-src 'self';
```

Chromium switches set before the app is ready: `disable-background-networking`, `disable-component-update`,
`disable-domain-reliability`, `disable-client-side-phishing-detection`, `disable-sync`, `disable-breakpad`,
`disable-crash-reporter`, `no-pings`, `disable-quic`,
`disable-features=DnsOverHttps,DnsOverHttpsUpgrade,AsyncDns,OptimizationHints,OptimizationGuideModelDownloading,MediaRouter,DialMediaRouteProvider,Translate,AutofillServerCommunication,CertificateTransparencyComponentUpdater,NetworkTimeServiceQuerying,InterestFeedContentSuggestions,WebRTC`,
`force-webrtc-ip-handling-policy=disable_non_proxied_udp`, `host-resolver-rules=MAP localhost 127.0.0.1, MAP * ~NOTFOUND`,
`proxy-server=<an address on this computer where nothing listens>`. After start: DNS over HTTPS off, the built-in
resolver off, the spell checker off with no languages and a dictionary address that goes nowhere.
Fonts: `system-ui, "Ubuntu Sans", "Ubuntu", "DejaVu Sans", sans-serif`. The window is created hidden and shown on its
first paint, its ready event or after 3 seconds, whichever comes first.
