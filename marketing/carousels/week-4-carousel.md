# Week 4 carousel — "A pre-launch checklist for production software"

**Account:** Xserv company page
**Format:** PDF carousel
**Slide count:** 10 slides

---

## Slide 1 — Cover

**Text:**
```
PRE-LAUNCH CHECKLIST
for production software

The things we check before any client system goes live.
```

---

## Slide 2

**Text:**
```
1. BACKUPS

Can we restore the database from yesterday in under 10 minutes?
Have we actually tested the restore, not just the backup?

If the answer to either is no, the system is not ready.
```

---

## Slide 3

**Text:**
```
2. MONITORING

Will we know if the system is down before the client tells us?
Are alerts going to a person, not a Slack channel nobody watches?
Is there an on-call rotation for the first 30 days?
```

---

## Slide 4

**Text:**
```
3. SECRETS

No secrets in code. No secrets in chat. No secrets shared via email.
A real secrets manager (or at minimum, environment variables not committed to the repo).

We have seen production credentials leaked in Slack on day one of more launches than we would like to admit.
```

---

## Slide 5

**Text:**
```
4. ACCESS

Who has admin access? Why?
Has the list been reviewed in the last week?
Is there a documented process for revoking access when someone leaves?

The first time you need this, you need it urgently.
```

---

## Slide 6

**Text:**
```
5. ROLLBACK

If today's deploy breaks production, can we roll back in under 5 minutes?

If the answer involves restoring a database from backup, the answer is no.
```

---

## Slide 7

**Text:**
```
6. THE FIRST USER ON DAY ONE

Who is going to actually log in first thing after launch?
Have they been trained?
Is there a phone number they can call if something is confusing?

A launch with no support plan is not a launch. It is a release.
```

---

## Slide 8

**Text:**
```
7. THE QUIET WEEK

Plan a quiet week after launch.
No new features.
No marketing campaigns that drive traffic.
The team's whole job for seven days is "watch what happens and fix what breaks."

Most clients want to skip this week. Refuse.
```

---

## Slide 9

**Text:**
```
WHAT TO DO IF ANY ITEM FAILS

Do not launch.

Genuinely. Slip the date. The cost of a bad launch is two months of customer trust. The cost of a one-week delay is one week.
```

---

## Slide 10 — CTA

**Text:**
```
We do production readiness reviews for clients launching new systems.

Two-day engagement, written report, specific gaps and how to fix them.

xservlabs.com

#xservlabs #productionsoftware
```

---

## Caption

```
The day we launch new software for a client is the day we are most nervous. Most software does not fail at scale. It fails on day one because someone forgot to check something boring.

This is the checklist we walk through before any system goes live.

Save it. Share with the team that runs your launches.

#xservlabs #productionsoftware
```

---

## First comment

```
If you have a launch coming up and want a fresh pair of eyes on your readiness, we do this as a paid two-day review. DM me.
```
