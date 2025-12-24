# ai-job-intelligence-engine
AI Job Intelligence Engine: turns job descriptions into structured insights + proposal-ready outputs using Python + LLM.
# AI Job Intelligence Engine (Upwork & Hiring Platforms)

This project is a production-grade AI automation system that converts raw job descriptions into structured hiring intelligence and proposal-ready outputs using Python and large language models.

It is designed for freelancers, recruiters, and hiring platforms that need to quickly understand job intent, complexity, and positioning — and generate high-quality responses automatically.

---

## What this system does

Given any job post, the engine automatically:

• Extracts the real hiring intent  
• Identifies key skills, complexity, and seniority  
• Generates a short, conversion-focused Upwork proposal  
• Produces a clean checklist of deliverables  
• Outputs recruiter-grade structured information  

This allows users to go from **job post → proposal → action plan** in seconds.

---

## How it works

1. A job description is loaded from a text file  
2. The Python engine builds a structured prompt  
3. The LLM (via Groq API) processes the job  
4. The system outputs a formatted proposal + checklist  

This is the same architecture used in real hiring automation tools and proposal engines.

---

## Files in this repository

| File | Purpose |
|------|--------|
| `job_automation.py` | Core AI automation engine |
| `jd.txt` | Sample transcription job |
| `sample_job.txt` | Sample Python automation job |
| `.env.example` | Environment variable template |

---

## How to run

1. Install dependencies  
```bash
pip install groq python-dotenv
