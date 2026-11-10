"""Fetch publicly viewable pages through the session's Chrome (CDP) and save raw HTML + ledger row.
Used only for pages that are publicly visible to an anonymous browser (abstract pages, OA articles).
Does not log in or bypass access controls."""
import sys, hashlib, csv, time
from datetime import datetime, timezone
from pathlib import Path
from playwright.sync_api import sync_playwright
sys.path.insert(0, str(Path(__file__).parent)); import search_literature as s

def main(pairs):
    with sync_playwright() as p:
        b = p.chromium.connect_over_cdp("http://localhost:29229")
        ctx = b.contexts[0]; pg = ctx.new_page()
        for url, out in pairs:
            ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
            try:
                r = pg.goto(url, wait_until="domcontentloaded", timeout=60000); time.sleep(6)
                st = str(r.status if r else "NA"); body = pg.content().encode()
                txt = pg.inner_text("body").encode()
            except Exception as e:
                st, body, txt = f"ERROR:{type(e).__name__}", b"", b""
            out = Path(out).resolve(); out.parent.mkdir(parents=True, exist_ok=True)
            if out.exists(): out = out.with_name(out.stem + "_" + ts.replace(":", "") + out.suffix)
            out.write_bytes(body); out.with_suffix(".txt").write_bytes(txt)
            for f in (out, out.with_suffix(".txt")):
                d = f.read_bytes()
                s.ledger_row(["chrome_cdp", url, ts, st, str(f.relative_to(s.ROOT)), len(d), hashlib.sha256(d).hexdigest(),
                              "Public page as shown to anonymous browser; LOCAL ONLY if copyrighted"])
            print(url, st, len(body), len(txt), flush=True)
        pg.close()

if __name__ == "__main__":
    a = sys.argv[1:]; main(list(zip(a[0::2], a[1::2])))
