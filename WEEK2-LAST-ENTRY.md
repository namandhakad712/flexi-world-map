# SAVE THIS FILE — the last Week 2 entry

> The platform sync overwrites `JOURNAL.md` on every pull, and this entry was
> entered a day past the Week 2 deadline (2026-10-19). It is preserved here
> so the 3+ hours of recorded work and the story of it can never be wiped by
> a sync. This is the raw entry text exactly as it should appear on the
> project page. Copy from here into the Half Life journal entry if it ever
> needs re-filing.
>
> **Hours: 3.0h** (on top of the previous 5.47h — Week 2 total **8.47h**)

---

## Entry title

**I actually finished it. (a day late, and it nearly killed me)**

## Entry body

Let me get the embarrassing part out of the way first: **today is October 19th. Week 2 ended yesterday.** I'm filing this because the last stretch of this project broke me a little and I refused to go to sleep with it unfinished. The last 3+ hours are on the timelapse and honestly they were the worst ones. i got the base layer done before — 1cm strips, 2mm slits, all planned out. then came the actual world map and it just. broke me.

the DXF hellscape. i downloaded SO many world map files and almost all of them were unusable. some were just lines — outlines with no closed shape so you can't extrude them into anything. some were literal dots?? opened the file and it was just a scatter of points like a printer having a seizure. some were all fused together so you'd select africa and get the entire atlantic along with it. and some had incomplete loops — the coastline would just stop, leave a gap, pick up somewhere else. a continent shaped like a broken moon.

for a bunch of those i actually had to draw the coastlines by hand. like close the loops myself in the sketcher. if you've never traced coastline by coastline at midnight it's this weird hypnotic soul-crushing thing. at one point i genuinely considered abandoning the map and just making a flexi rectangle and calling it abstract art. i did not. (i thought about it a LOT.)

eventually found one good file — a .txt of all things — that imported clean with actual closed shapes. i have no idea why the universe made the good one a text file. i was beyond asking questions by then.

then the real problem showed up. my base had the 2mm slits right, but the map layer had extruded as one solid slab. no slits at all. so it was just sitting on the base like a rug over a venetian blind — holding the whole thing stiff. which kills the entire point of the project. the flexi part. the rolling part. gone.

fixing it took forever because i could not explain it properly to gemini. i kept going back and forth — no the slits need to go through the map too, no wait not through, it just needs to be divided at the slit lines, no actually maybe through — and getting back a different wrong model each time. i was describing geometry with my hands at a monitor at 1am. we got there in the end: make the slits in the map solids the same way, then boolean union the whole thing into one part. slits line up, hinge lives, one flexible piece off the plate. i still don't know why that took 3 hours.

colors ended up as wood for the base and this chocolatey coffee brown for the map and it genuinely looks better than i planned?? it reads like an old explorer map that's been in someone's pocket for a century.

the map itself is not cartographically perfect. some coastlines are irregular, an island might be chunky. i know. i stared at them for hours. it stays — it's a map, not a navigation instrument.

in case my hours get questioned: the 3h in the lapse are real. scrub it and you'll watch the same map get imported, break, get hand-fixed, and re-imported like a dozen times. that's the work. it's late. it's done. and i'm going to sleep.

**What worked:** not quitting at the broken-map stage. the boolean union.
**What didn't:** every world map file on the internet, apparently, and my ability to describe boolean operations at 2am.

## Attachments

- Timelapse (3h+, the final stretch) — `lookout.hackclub.com` media link from the lapse recording
- Onshape public model link — goes in the project page / README
- Screenshots: the final unioned solid, the wood + coffee-brown color split
