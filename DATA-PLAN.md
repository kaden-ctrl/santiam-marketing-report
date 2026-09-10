# Santiam Hospital & Clinics — Social Media Report

**Reporting period:** January 1 – August 31, 2026
**Deliverable:** one-page visual report (charts, top posts, what's working / what's next)

## Accounts in scope

| # | Account | Platform |
|---|---------|----------|
| 1 | Santiam Hospital & Clinics | Facebook |
| 2 | Santiam Hospital & Clinics | Instagram |
| 3 | Santiam Hospital & Clinics | LinkedIn |
| 4 | Santiam Hospital & Clinics | X (Twitter) |
| 5 | Family Birth Center at Santiam Hospital | Facebook |

## Coupler.io pipeline

**Dataflow:** `Santiam Hospital & Clinics — Social Media (Jan–Aug 2026)`
`5f393c33-6249-460f-9f70-524671152e19`
https://app.coupler.io/app/dataflows/5f393c33-6249-460f-9f70-524671152e19/edit

Destination is the Claude connector, so report figures are queried straight from the
dataflow rather than exported to a sheet.

### Sources (7)

| Source | Report | Grain | Purpose |
|--------|--------|-------|---------|
| Facebook Page Insights | Page: performance insights | Monthly | Followers, new followers, page views, content views, post engagements, reactions |
| Facebook Page Insights | Post: posts lifetime performance | Per post | Top posts — likes, comments, shares, reactions, clicks, views |
| Instagram Insights | Profile: performance insights | Monthly | Reach, impressions, profile views, follows |
| Instagram Insights | Post: performance totals | Per post | Top posts |
| LinkedIn Company Pages | Page: performance insights | Monthly | Impressions, clicks, engagement rate |
| LinkedIn Company Pages | Page: follower gains trend | Monthly | Organic vs. paid follower gains |
| LinkedIn Company Pages | Post: individual posts lifetime performance | Per post | Top posts |

Credentials in use: Facebook `304716`, Instagram `304717`, LinkedIn `304718`.

### Status

All seven sources are fully configured and validated (`configured: true`), each scoped to the
correct Santiam account:

- Facebook — Santiam Hospital & Clinics (`621194984585316`) and Family Birth Center at
  Santiam Hospital (`1072957276097142`)
- Instagram — `santiamhospitalandclinics` (`17841400296120085`)
- LinkedIn — Santiam Hospital & Clinics (`74122166`)

A stray Facebook Ads (Meta Ads) source that appeared during wizard setup has been disabled;
it is not part of this report.

**Blocked.** A full run on 2026-09-10 failed on every dataset with:

> You've exceeded the maximum number of accounts allowed by your plan.
> Please upgrade to add more connections or disable an existing one.

The cap is enforced at the workspace level, not per dataflow — datasets scoped to a single
page fail identically to multi-page ones, so no amount of narrowing the dataflow clears it.
Resolving it requires a UI/billing action that the MCP surface does not expose (there is no
delete-credential tool):

1. Delete the failed all-in-one social template dataflow.
2. Delete the Google Analytics connection (`304719`) — unused by this report.
3. Re-run this dataflow.

If the cap persists after freeing those slots, the plan's account allowance is genuinely
below what four accounts require, and the choice is upgrading the plan or falling back to
manual CSV exports (Meta Business Suite covers Facebook and Instagram; LinkedIn and X each
export separately).

## Known data limitations

**X (Twitter).** The Coupler.io X source is public-data only. It returns publicly visible
engagement (likes, reposts, replies) and follower counts — it does **not** expose owner-only
analytics such as impressions or an impression-based engagement rate. No X credential is
connected. X figures, if included, are engagement-per-follower on public counts and are
labeled as such rather than presented as a like-for-like engagement rate against the other
three platforms. True X impressions require an X Analytics CSV export.

**Account cap.** The first attempt (via the all-in-one social template) failed with
"You've exceeded the maximum number of accounts allowed by your plan." That template pulls in
five sources including YouTube and Google Analytics. The replacement dataflow above is scoped
to the three platforms that matter, and the Google Analytics credential (`304719`) that the
template created is not needed for this report.

## Posting cadence (from the weekly social outlines)

Santiam Hospital FB 4 posts/week · IG 3/week · X 3/week · Family Birth Center FB 3/week.
(The Santiam Foundation FB/IG accounts are also managed weekly but are out of scope.)
