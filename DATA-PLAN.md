# Santiam Hospital & Clinics — Social Media Report

**Reporting period:** January 1 – August 31, 2026
**Deliverable:** one-page visual report (charts, top posts, what's working / what's next)

## Accounts in scope

| # | Account | Platform | Coupler.io source |
|---|---------|----------|-------------------|
| 1 | Santiam Hospital & Clinics | Facebook | `facebook-page-insights` |
| 2 | Santiam Hospital & Clinics | Instagram | `instagram-insights` |
| 3 | Santiam Hospital & Clinics | LinkedIn | `linkedin-public-data` |
| 4 | Santiam Hospital & Clinics | X (Twitter) | `twitter` |
| 5 | Family Birth Center at Santiam Hospital | Facebook | `facebook-page-insights` |

## Reports to pull per platform

**Facebook Page Insights** (both pages)
- `page_performance_insights`, split monthly — followers, new followers, reach, content views,
  post engagements, reactions
- `my_pages_post_statistics` — per-post lifetime performance, for the top-posts section

**Instagram Insights**
- `profile_performance_insights`, split monthly — reach, impressions, profile views, follows
- `post_insights_all_posts` — per-post totals for top posts
- `profile_account_overview` — lifetime follower count

**LinkedIn Company Pages**
- `pagePerformanceInsights`, split monthly — impressions, clicks, engagement rate
- `pageFollowerGainsTrend` — organic vs. paid follower gains
- `postsLifetimePerformanceInsights` — per-post performance for top posts

**X (Twitter) Public data**
- `entity: authors` — follower count
- `entity: tweets`, query `from:<handle>` — per-tweet likes, reposts, replies

## Known data limitation

The Coupler.io X source is **public data only**. It returns publicly visible engagement
(likes, reposts, replies) and follower counts — it does **not** expose owner-only analytics
such as impressions or the impression-based engagement rate. X figures in the report are
therefore engagement-per-follower, computed on public counts, and are labeled as such rather
than being presented as a like-for-like engagement rate against the other three platforms.

## Setup status

Coupler.io workspace is empty — no credentials, no dataflows, no datasets. Blocked on the
one-time browser authorization for each provider:

- Facebook — https://app.coupler.io/app/connections/facebook/new
- Instagram — https://app.coupler.io/app/connections/instagram/new
- LinkedIn — https://app.coupler.io/app/connections/linkedin/new
- X (Twitter) — https://app.coupler.io/app/connections/twitter/new

Page/profile selection happens in the Coupler.io wizard and cannot be automated.

## Posting cadence (from the weekly social outlines)

Santiam Hospital FB 4 posts/week · IG 3/week · X 3/week · Family Birth Center FB 3/week.
(The Santiam Foundation FB/IG accounts are also managed weekly but are out of scope for
this report.)
