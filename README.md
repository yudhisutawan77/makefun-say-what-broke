# Say What Actually Broke

![make.fun](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)
![rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/yudhisutawan77/makefun-say-what-broke/rank.svg)
![reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/yudhisutawan77/makefun-say-what-broke/reward.svg)

[make.fun bounty: Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

One line of error copy, at most 200 characters, that tells the user the
brutal truth about what went wrong — and makes them laugh on the way.
The judge brief: name the real failure in plain words, be funny on a
single read, and survive being pasted into a real product's error dialog.

## The entry

> Your payment went through. Your order didn't. Your money is safe in our account; your order is nowhere. Email support and bring patience — you'll need it.

**154 characters** (limit: 200, single line).

Why this line: it names a failure every shopper recognises — the money
cleared, the order vanished — instead of hiding behind "something went
wrong". The twist ("your money is safe in *our* account") is the joke,
and the last beat tells the user exactly what to do next.

## How it works

`main.py` writes the entry to `/output/entry.txt` and exits non-zero
if the line is empty, multi-line, or over 200 characters:

```sh
python3 main.py
cat /output/entry.txt
```
