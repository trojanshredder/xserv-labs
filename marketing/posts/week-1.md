# Week 1 posts

5 text posts. Each is ready to paste into LinkedIn directly. Image suggestions noted where relevant.

---

## Monday — Founder personal

**Topic:** The cost of switching dev tools too often
**Account:** Founder personal

```
There's a particular kind of slow damage that small companies do to themselves by switching tools every six months.

We switched issue trackers four times between 2020 and 2023. Trello, Jira, Linear, Notion, back to Jira, finally Linear again. Each switch took two weeks of nobody-knows-where-anything-is. Every old ticket lost half its context. Knowledge that lived in comments got abandoned.

The new tool was always slightly better. The cost of switching was always larger than the slightly-better.

We do this now: a tool stays for two years minimum, no matter what. If something is genuinely broken we fix the process around it rather than the tool. Most "tool problems" turn out to be process problems wearing tool-shaped clothes.

The thing I keep relearning is that boring continuity beats exciting churn. Doubly so for anything the whole team uses.

#xservlabs
```

---

## Tuesday — Engineering perspective

**Topic:** Why we still use Postgres for almost everything
**Account:** Founder personal (engineer-authored, posted under founder's name with attribution in the post)

```
Posted on behalf of [Engineer name] who runs most of our backend work:

Every six months somebody on the team asks if we should be using something other than Postgres for [specific workload]. Time-series? Maybe Timescale. Search? Maybe Elastic. Queue? Maybe Kafka. Document store? Maybe Mongo.

The answer is almost always: just use Postgres.

Postgres has time-series extensions, full-text search, JSON columns, a job queue pattern that works for 95% of cases, and the operational discipline of a 30-year-old database that has fewer surprise failures than anything younger.

The hidden cost of running 4 different stateful systems in production is not the licensing. It is the operational complexity. Each one has its own backup story, its own failure mode, its own version upgrade pain. We have seen small teams disappear under the weight of running specialised infrastructure they didn't actually need.

The wisest senior engineer I know once said the best database is the one that's already running and the team already knows. He was right.

#xservlabs #postgres
```

---

## Thursday — Traxium product

**Topic:** What customers actually use Traxium for vs what we thought
**Account:** Traxium company
**Image suggestion:** A simple comparison graphic — "What we built it for" vs "What customers use it for"

```
When we started building Traxium, we assumed customers would mostly use the live tracking dashboard. The big map. The thing that shows where every truck is in real time.

A year in, we have data on what customers actually open. Here is what we have learned.

The dashboard is the fourth most-used feature. The top three are:

1. WhatsApp alerts. Most customers do not open the dashboard during the day at all. The alerts find them.
2. The trip history tab. Showing what happened yesterday, last week, last month, with reasons for delays. Used heavily on Mondays.
3. The document expiry view. Looked at once a week, prevents at least one renewal panic per month per customer.

We have rebuilt the homepage around this. The dashboard is still available but it is not the first thing you see. The first thing you see is alerts that need action and documents that need attention.

If you operate a fleet and you have not tried Traxium, the first month is free.

traxium.in

#traxium #logistics
```

---

## Friday — Founder personal

**Topic:** The Friday afternoon problem
**Account:** Founder personal

```
Every software company I have worked with or run has had the same Friday afternoon problem.

At 4 PM on a Friday, somebody asks "can we just push this small change before the weekend." Sometimes it is the client. Sometimes it is somebody on the team. The change is described as small.

It is almost never small. It is small in the moment. It becomes large somewhere between 6 PM Friday and 9 AM Monday.

We have a rule now. No deployments after 2 PM on a Friday unless there is a fire that demands one. Everything else waits until Monday morning. The cost of a wrong deploy at 4 PM Friday is the entire weekend of two engineers. The cost of waiting until Monday is a weekend.

The other thing I have noticed is that the "small Friday change" is rarely critical. The pressure to ship it is almost always internal, not external. The client has not asked for it by Friday afternoon. We have invented the urgency.

Block your Friday afternoons. The weekend you save is your own.

#xservlabs #founderlife
```

---

## Monday backup option (use if the dev tools post does not fit)

**Topic:** A specific industry trend take
**Account:** Founder personal

```
Quietly happening in Indian logistics tech: small fleet operators (20-50 vehicles) are starting to adopt software at a rate I did not expect to see for another two years.

For most of the last decade this segment was a black hole. Too small for the enterprise PMS vendors to bother with. Too operationally complex for the consumer-grade tracking apps. So they ran on spreadsheets and WhatsApp groups, like everyone else.

What changed: UPI normalised digital payments for them. GST normalised digital invoicing. Wheelseye and similar made GPS standard. Now the gap between "we run on spreadsheets" and "we could run on software" is smaller than it has ever been.

I think the next 18 months are going to be the loudest in Indian logistics tech we have seen. Lots of new products, lots of failed ones, a handful of category winners. The operators who pick well are going to leave the ones who do not pick at all behind in a way they cannot catch up from.

#xservlabs #logistics #indiantech
```
