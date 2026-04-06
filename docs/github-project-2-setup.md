# GitHub Project #2 Setup (Cloud-first)

This repository now includes a **cloud workflow** so you do not need to run setup on your local machine.

## Recommended path (no local setup)

1. In GitHub, open this repository's **Settings → Secrets and variables → Actions**.
2. Create a secret named `PROJECT_SETUP_TOKEN` with a PAT that has:
   - `repo` scope (for issues/labels)
   - `project` scope (for ProjectV2 item operations)
3. Go to **Actions → Setup GitHub Project #2 → Run workflow**.
4. Keep defaults (`owner=intiequals1`, `project_number=2`) and run.

Workflow file: `.github/workflows/setup-project2.yml`.

## What the cloud workflow does

- Ensures baseline labels exist.
- Finds or creates the baseline backlog issues (idempotent by exact title).
- Adds each issue to `https://github.com/users/intiequals1/projects/2`.

## Baseline issues seeded

- P0: Audit missing POC files under `product/system/poc_with_triggers`
- P0: Import first safe POC batch with explicit placeholders
- P1: Resolve `test.txt` artifact (remove or justify)
- P1: Add/verify smoke tests and align CI with real paths
- P2: Continue Webex adapter in small, controlled increments

## Notes

- The workflow is idempotent for issue creation and project item add operations.
- If your project owner is an org instead of a user, adjust the GraphQL lookup accordingly.

## Make Project #2 accessible without sign-in

If you want anyone (including unauthenticated environments) to view the board in the browser:

1. Open `https://github.com/users/intiequals1/projects/2`.
2. Click **...** (top-right) → **Settings**.
3. Set **Visibility** to **Public**.
4. Ensure the linked repository is also publicly readable (or viewers have read access), otherwise item content can still be restricted.

### Important limitation

- GitHub API/CLI operations that mutate project data (create items, update fields, etc.) still require authentication, even if the project is public.
- Public visibility improves read access in the browser; it does not remove token requirements for automation writes.

### Quick verification

- Browser: open the project URL in a private/incognito window.
- CLI (read check): `gh project view 2 --owner intiequals1`

