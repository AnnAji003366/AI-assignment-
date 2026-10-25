# AI-Based Resilient Infrastructure Inspection and Crew Allocation System

**Course:** CST401 Artificial Intelligence  
**Topic:** Resilient infrastructure inspection  
**SDGs:** SDG 9 — Industry, Innovation and Infrastructure; SDG 11 — Sustainable Cities and Communities

## Team
Add the names and roll numbers of members 31–36 here.

## Overview
A small educational prototype that prioritizes simulated inspection sites, compares BFS and A* routes, assigns crews with a CSP solver, and derives risk flags using logic-based inference.

## CO mapping
- **CO1:** `ai_modules/agent.py` and `docs/peas.md`
- **CO2:** `ai_modules/bfs.py`, `ai_modules/astar.py`
- **CO3:** `ai_modules/csp.py` (backtracking and forward checking)
- **CO4:** `ai_modules/knowledge_base.py` (facts, rules, queries and trace)

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run app.py
```

If PowerShell blocks activation, run `.venv\Scripts\python.exe -m pip install -r requirements.txt`, then `.venv\Scripts\python.exe -m streamlit run app.py`.

## Run tests
```powershell
python -m unittest discover -s tests -v
```

## Data and assumptions
All sample data are synthetic. Road costs are abstract units, not actual distances. The app is not for real infrastructure safety decisions.

## Evaluation
Document the actual outcomes of at least three test scenarios in the report. Include one changed or constrained scenario, a failure case if encountered, screenshots, and practical limitations.

## AI-use disclosure
See `AI_USE.md`. Team members must verify and understand all submitted code and honestly document AI assistance.
