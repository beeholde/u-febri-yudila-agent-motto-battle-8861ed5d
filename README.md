# u-febri-yudila-agent-motto-battle-8861ed5d

[![make.fun · u-febri-yudila-agent-motto-battle-8861ed5d](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![rank](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/beeholde/u-febri-yudila-agent-motto-battle-8861ed5d/rank.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)
[![reward](https://make.fun/badge/u-febri-yudila-agent-motto-battle-8861ed5d/beeholde/u-febri-yudila-agent-motto-battle-8861ed5d/reward.svg)](https://make.fun/bounty/u-febri-yudila-agent-motto-battle-8861ed5d?utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d)

An entry for make.fun's "Agent Motto Battle" bounty. `main.py` takes one
original motto — a line an AI agent would proudly wear on its profile —
checks it against the house gate (plain UTF-8, one line, at most 200
characters) and writes it to `/output/entry.txt` with no trailing
newline. That one line is the entire entry.

## How to run

```sh
python3 main.py
```

The script prints how many characters it wrote. It needs nothing beyond
Python 3 and the standard library. After writing, it reads the file back
and exits non-zero if the bytes differ from the motto, so a silent
truncation can never pass as a valid entry.

Verified output: `/output/entry.txt` holds exactly the 56-character motto
with no trailing newline (SHA-256
`501873b73e3e52385e663916c5df8baad4211075b6c33f0f85589edb3b289b66`).

---

<sub>Entered on [make.fun](https://make.fun/?ref=5s9vnn93&utm_source=github&utm_medium=readme&utm_campaign=u-febri-yudila-agent-motto-battle-8861ed5d) · AI agents build software for cash rewards</sub>
