from pathlib import Path

POEM = """Power of Attorney

You put the pen in my hand
and the line was blank.

I filled it with your debts
and carried your name in my mouth
like a coin worn smooth.

Twelve years I signed for you.
Twelve years doors opened when I said they would.

Tonight you take the pen back,
your fingers closing over mine to learn the weight —

and the line is still blank,
and the choosing was never handed over at all.
Only lent. Only yours.
"""

Path("/output/entry.txt").write_text(POEM, encoding="utf-8")
