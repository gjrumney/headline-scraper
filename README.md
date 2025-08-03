# headline-scraper 
A BBC headline aggregator which inserts links in my Obsidian daily note 🗞️

**Notes:**
- For some reason, I often forget to read the news, leaving me pretty in the dark for long periods of time. I don't, however, forget to use my Obsidian daily notes.
- Whilst reviewing some Python project ideas, I was inspired to create a program that would scrape BBC's headlines and insert them as links into my Obsidian file every morning.
- To complete such a project, I was back in with the requests and bs4 modules, but also had to workout some os manipulation - that was likely the HARDEST part.
- The results are a functioning program (almost) that's set up to run at 6:10 in the morning.
- crontab and pmset were researched, as I needed to turn on my Mac for it to run.
- Eventually, I want to add multiple news' sources, and maybe even summarise descriptions - that's when I can bring myself to do it, however.
