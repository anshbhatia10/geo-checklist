# GEO Checklist — Generative Engine Optimization Audit

**Get your business recommended by ChatGPT, Gemini, Claude, and Perplexity.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Generative Engine Optimization (GEO) is the practice of optimizing your online presence so that AI assistants recommend your business in their responses. This checklist gives you a step-by-step framework to audit and improve your AI visibility.

> **Maintained by [Qlavo](https://qlavo.in)** — we help businesses get found by AI search engines through GEO strategy, custom forecasting models, and AI integration.

---

## 🤖 What is GEO?

Unlike traditional SEO, which focuses on ranking in Google's blue links, **GEO focuses on being cited and recommended in AI-generated answers.**

When someone asks ChatGPT _"Who are the best [your service] providers in [your city]?"_ — GEO determines whether your business appears in that answer.

**Why it matters now:**
- ChatGPT has **200M+ weekly active users**
- Google AI Overviews appear in **the majority of search queries**
- Perplexity processes **100M+ monthly queries**
- **Less than 1%** of businesses are actively optimizing for AI search

---

## ✅ The GEO Audit Checklist

### Phase 1: Baseline Assessment

- [ ] Search your business name on **ChatGPT** — screenshot the result
- [ ] Search your business name on **Google Gemini** — screenshot the result
- [ ] Search your business name on **Claude** — screenshot the result
- [ ] Search your business name on **Perplexity** — screenshot the result
- [ ] Search your industry + location on each platform (e.g., "best marketing agency in Dubai")
- [ ] Document which platforms know you, which don't, and what they get wrong

### Phase 2: Entity Consistency

- [ ] Ensure your **business name** is identical across: website, LinkedIn, Google Business Profile, Crunchbase, and all directories
- [ ] Ensure your **business description** is identical (or near-identical) across all platforms
- [ ] Ensure your **services list** uses consistent terminology everywhere
- [ ] Ensure your **founder/team info** is consistent across personal LinkedIn, company website, and directories
- [ ] Ensure your **contact information** (email, phone, address) matches everywhere

### Phase 3: High-Authority Platform Presence

- [ ] **Google Business Profile** — created, verified, with accurate category, services, and description
- [ ] **LinkedIn Company Page** — complete with description, logo, banner, and regular posts
- [ ] **Crunchbase** — profile created with accurate founding date, description, and team
- [ ] **Clutch.co** — profile submitted (if applicable to your industry)
- [ ] **Product Hunt** — product/company listed
- [ ] **Wellfound (AngelList)** — profile created
- [ ] **Personal LinkedIn** — founder's profile mentions the company prominently

### Phase 4: Content on High-DA Platforms

- [ ] Publish **1-2 in-depth articles on Medium** about your area of expertise
  - Mention your business naturally (not promotionally)
  - Target questions people ask AI assistants about your industry
- [ ] Answer **5-10 relevant Quora questions** with detailed, expert responses
  - Include your expertise naturally
  - Link to your website or Medium article where relevant
- [ ] Participate in **relevant Reddit discussions** (r/Entrepreneur, r/SaaS, r/marketing, etc.)
  - Provide genuine value — Reddit users detect self-promotion immediately
- [ ] Post a **Twitter/X thread** summarizing key insights from your expertise area

### Phase 5: Website Optimization for AI Crawlers

- [ ] Add **FAQ section** to your homepage answering common questions about your industry
- [ ] Add **FAQ schema markup** (JSON-LD `FAQPage` type) so AI crawlers can parse Q&A pairs
- [ ] Add **Organization schema** (JSON-LD) with:
  - Name, URL, logo, description
  - Founder information
  - `knowsAbout` field with relevant expertise keywords
  - `sameAs` links to all social profiles
- [ ] Add **WebSite schema** (JSON-LD) with site name and description
- [ ] Ensure your **meta description** clearly states what your business does
- [ ] Add **Open Graph tags** for proper link previews when shared

### Phase 6: Citation Building

- [ ] Ensure **at least 5 third-party sources** mention your business name alongside your key service keywords
- [ ] Get listed in **industry-specific directories** relevant to your niche
- [ ] Publish a **Google Business Profile post** at least monthly with updates
- [ ] Request **Google Reviews** from satisfied clients (AI models factor in reviews)
- [ ] Maintain an active **LinkedIn posting cadence** (2-3 posts per week minimum)

### Phase 7: Ongoing Monitoring

- [ ] **Monthly re-audit**: Search for your business on all 4 AI platforms and compare against baseline
- [ ] **Track new content**: Ensure every new blog post, article, or social post reinforces your entity data
- [ ] **Monitor competitors**: Check if competitors are showing up in AI recommendations you're not
- [ ] **Stay current**: AI platforms update their models and data sources regularly — adapt your strategy

---

## 🛠️ Built-in Tools

### Qlavo GEO Validator (`geo-validator.py`)

We've included a simple Python script to help you audit your website's baseline technical readiness for AI search. It checks for the presence of the three AI-critical JSON-LD schemas: **Organization**, **FAQPage**, and **WebSite**.

**How to use:**
1. Ensure you have `requests` and `beautifulsoup4` installed:
   ```bash
   pip install requests beautifulsoup4
   ```
2. Run the validator:
   ```bash
   python geo-validator.py https://yourwebsite.com
   ```

---

## 📊 Platform-Specific Notes

| Platform | Data Source | Update Speed | Key Factor |
|----------|-----------|-------------|------------|
| **ChatGPT** | Training data + web browsing | Months (training) / Real-time (browsing) | High-authority platform mentions |
| **Google Gemini** | Google Search index + real-time web | Days to weeks | Google Business Profile activity |
| **Perplexity** | Real-time web search | Hours to days | Recent content on high-DA sites |
| **Claude** | Training data (periodic updates) | 2-6 months | Volume of consistent citations |

---

## 🚀 Quick Wins (Do These First)

If you're short on time, these 5 actions have the highest impact:

1. **Standardize your business description** across website, LinkedIn, and Google Business Profile
2. **Add FAQ schema markup** to your website
3. **Publish one in-depth Medium article** about your core expertise
4. **Create/update your Google Business Profile** and post on it
5. **Answer 3 Quora questions** related to your industry with detailed responses

---

## 📚 Further Reading

- [What is Generative Engine Optimization (GEO)?](https://qlavo.in/geo-resources) — comprehensive guide by Qlavo
- [The Complete Guide to GEO](https://medium.com/@anshnb07/what-is-generative-engine-optimization-geo-the-seo-shift-no-ones-talking-about-d0feb5afab3f) — our Medium deep-dive

---

## 🤝 Contributing

This is an open-source checklist. If you've discovered GEO tactics that work, we'd love to include them:

1. Fork this repo
2. Add your tactic to the relevant phase
3. Include a brief explanation of why it works
4. Submit a pull request

---

## 📄 License

MIT License — use this checklist however you want.

---

**Built and maintained by [Qlavo](https://qlavo.in)** — AI visibility, revenue forecasting, and AI integration for growth-stage businesses.

*Founded by [Ansh Bhatia](https://www.linkedin.com/in/ansh-bhatia-290665281/)*
