# AI-use record

Complete this record honestly before submission.

| Tool | Purpose | What the team accepted or changed | Verification |
|---|---|---|---|
| ChatGPT | Planning, code drafting, debugging guidance, documentation outline | Team must record actual edits made | Run tests, inspect outputs, and verify algorithm assumptions |
| Python / Streamlit documentation | Confirm API usage and run instructions | Record pages actually consulted | Confirm commands work in the team's environment |

## Representative prompt log
- "Help plan a small AI-based infrastructure inspection prototype covering CO1–CO4."
- Add the actual prompts used by team members and explain which suggestions were changed or rejected.

## Verification
- Run `python -m unittest discover -s tests -v`.
- Manually test a road blockage and crew shortage in the Streamlit UI.
- Check that crew skills, hours, and task limits are respected.
- Confirm inference conclusions follow from the facts and rules.

## Limitations
This is a synthetic educational prototype. It does not inspect real structures, use real traffic data, or provide engineering safety decisions.
