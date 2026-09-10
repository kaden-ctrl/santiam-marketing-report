# Handoff — moving this work from the cloud container to a local session

Written 2026-09-10. Read this first if you're picking the report up on your own machine.

## The goal

A **one-page social media report for Santiam Hospital & Clinics**, covering
**Jan 1 – Aug 31, 2026**: charts and graphs, top posts, page growth, new followers,
likes/shares, engagement rate, plus "what's working" and "what we're working on."

Five accounts:

| # | Account | Platform |
|---|---------|----------|
| 1 | Santiam Hospital & Clinics | Facebook |
| 2 | Santiam Hospital & Clinics | Instagram |
| 3 | Santiam Hospital & Clinics | LinkedIn |
| 4 | Santiam Hospital & Clinics | X (Twitter) |
| 5 | Family Birth Center at Santiam Hospital | Facebook |

**No report has been built yet.** Not a single real metric was ever obtained. Everything
below is groundwork and dead-end elimination.

## What was tried, and what happened

### 1. Google Drive — no social analytics exist
Searched thoroughly. Drive holds Google Ads performance sheets, weekly content outlines,
blog posts, and email blasts. The one social KPI tracker found (`2025 Monthly KPI Tracker`)
belongs to a different client set entirely (Performance Health, THERABAND, Cramer). Useful
only as a **format reference** — it tracks Followers, Reach, Impressions, Engagements,
Eng. Rate, Clicks, Posts, each with a prior-month delta. That's a good shape for this report.

### 2. Coupler.io — built, correct, and blocked on billing
A dataflow was created and fully configured. See `DATA-PLAN.md` for full detail.

- Dataflow `5f393c33-6249-460f-9f70-524671152e19`
- Seven sources across Facebook / Instagram / LinkedIn, monthly page metrics plus per-post
  detail, all dated Jan 1 – Aug 31 2026
- All seven validate (`configured: true`) with the correct Santiam pages selected
- Destination is the Claude connector, so a successful run is queryable directly

Every run fails on every dataset with:

> You've exceeded the maximum number of accounts allowed by your plan.

The cap is **workspace-level**. Datasets scoped to a single page fail identically to
multi-page ones, so no dataflow change clears it. **Moving local does not fix this** — it is
a billing limit on the Coupler account, not an environment restriction.

To clear it: delete the failed all-in-one template dataflow, delete the unused Google
Analytics connection (`304719`), then re-run. If it still caps, the plan allowance is below
the four accounts required and it needs an upgrade.

### 3. See Through Dashboard — wrong data, permanently
`seethroughtracking.duogroup.com` is Duo Group's Agency Analytics replacement (Next.js +
Supabase). Its source archive is in Drive and was reviewed.

**It is a paid-advertising portal only.** `metric_snapshots` stores spend, impressions,
clicks, conversions, conversion value, CPC, CPA, ROAS. `platform_connections` supports
`google_ads`, `meta_ads`, `linkedin_ads`. There are **no organic fields anywhere** — no
followers, engagement rate, reactions, shares, saves, or per-post organic performance.

**Moving local does not fix this either.** The data isn't there to fetch. See Through stays
the right home for Santiam's *ads* reporting; it can never answer this report.

### 4. Browser access — the one blocker that IS environmental
The cloud container could not reach `seethroughtracking.duogroup.com` at all (network policy
returns 403 at the proxy), and its headless Chromium holds none of the logged-in sessions for
Meta Business Suite or LinkedIn.

## What actually changes when you run locally

| Blocker | Fixed by going local? |
|---|---|
| No logged-in browser sessions | **Yes** — your own browser is already signed in |
| `seethroughtracking.duogroup.com` unreachable | **Yes** — no agent proxy in the way |
| Coupler.io account cap | **No** — billing limit on the account |
| See Through has no organic data | **No** — the data does not exist |

So going local solves the *access* problem, which is the one that matters: it puts the
exports one click away, and lets a local session drive a real browser profile if you want
that automated.

## Picking this up locally — do this

1. **Clone and read the two docs**
   ```bash
   git clone https://github.com/kaden-ctrl/santiam-marketing-report
   cd santiam-marketing-report
   git checkout claude/santiam-hospital-social-report-ep797r
   ```
   `DATA-PLAN.md` has the full Coupler configuration and the metric-by-metric plan.

2. **Get the numbers.** Fastest path, roughly five minutes:
   - Meta Business Suite → Insights → Export. One file covers **both** Facebook pages *and*
     Instagram. Date range Jan 1 – Aug 31 2026.
   - LinkedIn → Santiam Hospital & Clinics page → Analytics → Export (visitors, followers,
     updates).
   - X → follower count and top posts. Public engagement only unless you export from
     X Analytics.

3. **Hand the files to a local Claude Code session** with a prompt like:
   > Build the Santiam Hospital & Clinics one-page social report for Jan–Aug 2026 from these
   > exports. Follow DATA-PLAN.md. Charts for page growth and engagement rate by month per
   > platform, a top-posts section, and What's Working / What We're Working On.

4. **Optional — the durable fix.** Clear the Coupler cap (step in §2 above) and the dataflow
   already built takes over, making this monthly and automatic for Santiam and every other
   client.

## Known limitation to carry forward: X (Twitter)

Coupler's X source is **public data only** — it returns likes, reposts, replies and follower
counts, but **not impressions**, so it cannot produce a true engagement rate comparable to the
other three platforms. No X credential was ever connected. Either report X as
engagement-per-follower and label it plainly, or export from X Analytics for real impressions.

## Security — act on this regardless

The `See Through Dashboard.zip` in Google Drive contains a populated `.env.local`. Its values
were never read and the working copy was shredded, but these are real credentials sitting in
Drive:

- `TOKEN_ENCRYPTION_KEY` — decrypts every stored OAuth token in the Supabase database
- `SYNC_SECRET`, `REVALIDATE_SECRET`
- `GOOGLE_ADS_CLIENT_ID`, `GOOGLE_ADS_CLIENT_SECRET`

Rotate them and delete the archive. The repo's `.gitignore` excludes `.env.local`; the zip was
made by archiving the folder, which bypasses it.

## Useful context already gathered

Posting cadence, from the weekly social outlines — use it for "what we're working on":
Santiam Hospital FB **4 posts/week** · IG **3/week** · X **3/week** ·
Family Birth Center FB **3/week**. The Santiam Foundation FB/IG accounts run on the same
weekly rhythm but were left out of scope.
