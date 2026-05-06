#!/usr/bin/env python3
# Author: BleakNarratives | File: askhole.py | Path: /storage/ED7B-AD5A/root_2026/askhole-cli/askhole.py
import os, sys, subprocess

VERSION = "2.0.0"
HOME = os.path.expanduser("~")
SD = "/storage/ED7B-AD5A/root_2026"

def assess():
    print("[+] Assessing stack...")
    targets = {
        "ws_server": f"{HOME}/ws_server.py",
        "AutoDNA": f"{HOME}/autodna/engine.py",
        "Pancho": f"{HOME}/bin/pancho.sh",
        "Codemate": f"{HOME}/bin/codemate",
        "Higgins Bot": f"{HOME}/bin/higgins_telegram.py",
        "Listener": f"{HOME}/passive_income_swarm/nostr_dvm/bin/listener.py",
        "Mrs Higgins": f"{SD}/Mrs-Higgins",
        "ZeroClaw DB": f"{HOME}/.zeroclaw_genetic/arena.db",
        "Boardroom HTML": f"{SD}/Vertical-AI/equinex_v2.html",
        "Meatboard": f"{SD}/meatboard.html",
        "GREENROOM": f"{HOME}/GREENROOM_HANDOFF.md",
    }
    for name, path in targets.items():
        found = os.path.exists(path)
        status = "[92m[FOUND][0m" if found else "[91m[MISSING][0m"
        print(f"  {status} {name}")

def services():
    print("[+] Services...")
    for s in ["ws_server.py","listener.py","webhook_server.py","higgins_telegram.py","codebase_evolution_daemon.py"]:
        pid = subprocess.run(["pgrep","-f",s],capture_output=True,text=True).stdout.strip()
        st = f"[92m[LIVE {pid}][0m" if pid else "[91m[DEAD][0m"
        print(f"  {st} {s}")

def start():
    subprocess.Popen(f"PYTHONPATH={SD}/vertical_ai:{HOME} nohup python3 {HOME}/ws_server.py >> {HOME}/ws_server.log 2>&1",shell=True)
    subprocess.Popen(f"nohup python3 {HOME}/passive_income_swarm/nostr_dvm/bin/listener.py >> {HOME}/nostr_listener.log 2>&1",shell=True)
    subprocess.Popen(f"nohup python3 {HOME}/bin/higgins_telegram.py >> {HOME}/higgins_telegram.log 2>&1",shell=True)
    print("Fired. Check services.")

def greenroom():
    import datetime
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    txt = f"""# GREENROOM {ts}
## LIVE: listener.py, webhook_server.py, ws_server PID 1055
## FIX: ws_server needs PYTHONPATH={SD}/vertical_ai at launch
## MELISSA: send meatboard.html, text menu to Mrs_Higgins_bot
## BUGS: molt_watchdog line 290, molt_prog placeholder, ~/~ 3.3GB
## NEXT: askhole v2 deployed, read codebase_evolution_daemon.py together
"""
    open(f"{HOME}/GREENROOM_HANDOFF.md","w").write(txt)
    print(f"Written.")

cmds = {"assess":assess,"services":services,"start":start,"greenroom":greenroom}
if len(sys.argv)>1 and sys.argv[1] in cmds:
    cmds[sys.argv[1]]()
else:
    print("Usage: askhole [assess|services|start|greenroom]")
