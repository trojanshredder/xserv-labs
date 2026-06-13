# Week 3 posts

---

## Monday — Founder personal

**Topic:** Why most internal tools fail
**Account:** Founder personal

```
Most internal tools at small-to-mid companies fail in roughly the same way.

Somebody on the operations team builds a Google Sheet that solves a problem. It works. People use it. Six months later it has 14 tabs, three pivot tables nobody understands, references to a tab someone deleted, and the founder asks engineering to "just turn this into a proper tool."

Engineering builds the proper tool. Three months of work. Beautiful UI. Modeled after the spreadsheet. Six weeks after launch the operations team is back on a new spreadsheet.

The thing that killed the tool was not the engineering. It was that the spreadsheet was load-bearing in ways nobody had documented. The operations team did not just use it to store data. They used the comments on rows to coordinate. They used colour codes to flag priorities that had no formal field. They used the find-replace shortcut to do bulk updates the new tool did not support.

Internal tools fail when engineering rebuilds the data model and forgets to rebuild the social model around it.

What works: ship the new tool with the spreadsheet still working. Move people over one workflow at a time. Watch what they keep doing in the spreadsheet that the tool cannot do. That gap is the actual product.

#xservlabs #internaltools
```

---

## Tuesday — Engineering perspective

**Topic:** Three Postgres extensions that changed how we build
**Account:** Founder personal (engineer voice)

```
Three Postgres extensions that are quietly carrying a lot of our production systems:

1. pgvector. We started using this when one client wanted semantic search across their support tickets. It is now in three of our codebases for various "find documents like this one" features. Beats running a separate vector database for almost any workload under a few million embeddings.

2. pg_cron. Schedules jobs inside Postgres itself. We used to run a separate worker process for periodic tasks. Now most "send this email every Monday morning" or "recompute this aggregate every hour" lives in pg_cron. Less infrastructure to monitor.

3. pg_stat_statements. Comes built into most managed Postgres deployments but you have to enable it. Once enabled, it tells you which queries are slow, how often they run, and which indexes you are missing. Saved us about a week of investigation work on a client database last month.

None of these are exciting. All of them have removed an entire piece of infrastructure from our stack at some point. The pattern is: most "we need a new service for X" problems are solvable inside the database we already have.

#xservlabs #postgres
```

---

## Thursday — Traxium product

**Topic:** The control room that doesn't need a control room
**Account:** Traxium company
**Image suggestion:** A photo of an empty desk or an unstaffed control room screen, or a phone showing a WhatsApp alert

```
A customer told us last week they had stopped staffing their control room overnight.

For context, they run a 60-vehicle fleet doing mostly intercity night runs across south India. Three years ago they had two people on overnight shifts watching the GPS dashboard and answering driver calls. Two years ago, after a near-incident, they added a third. Six months ago they cut back to one and were considering hiring a fourth. Today they have zero people watching overnight.

What happened was Traxium. Every alert that the night shift used to be there to catch — vehicle stopped too long, driver fatigue, document expiry, delivery delayed — now pings the operations head's phone on WhatsApp. He gets maybe two pings a night. He sleeps through the quiet ones.

The cost savings are real. Two salaries plus night-shift differentials, recovered. But the customer said something more interesting. The night shifts were also where stress was concentrated. Watching dashboards is a particular kind of exhausting that nobody talks about. Removing it as a human task improved morale beyond just the cost line.

If you have someone watching screens all night who could be doing something better, we should talk.

traxium.in

#traxium #logistics
```

---

## Friday — Founder personal

**Topic:** A small client moment
**Account:** Founder personal

```
A client called me last Tuesday to ask if we had time for a quick call. I assumed something was broken.

When the call connected, he said: "I just wanted to say that the system has not gone down once in eight months. I noticed because my old vendor's system used to go down on the 28th of every month and I had stopped scheduling things on the 28th. I scheduled something this 28th. It went fine. I just wanted you to know."

That was the whole call. Maybe four minutes. He hung up.

I keep thinking about it because it is the kind of feedback nobody asks for and nobody plans to give. He noticed because his calendar pattern had changed. He called because he is the kind of person who calls.

I have been doing this work in some form for years and the most validating thing anyone has said about my team's work was an unscheduled four-minute phone call about a system that nobody had to think about anymore.

This is the goal. Not awards. Not posts about us in trade publications. A system so reliable that customers reorganise their calendars around how reliable it is, and then call to tell you.

#xservlabs
```
