# virtual-user-ai

Virtual User AI is a v1 POC for an AI meeting participant with one shared core and platform adapters.

Current imported code covers:
- shared trigger/policy/orchestration core
- media contract boundary with local dry-run implementations
- Webex adapter as the first real adapter track (dry-run capable)
- smoke tests validating audio path and chat fallback behavior

Not complete yet:
- credential-backed Webex operations (join/chat control paths)
- Teams/Zoom/Meet adapters
- production-grade media injection setup
