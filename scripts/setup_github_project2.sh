#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   OWNER=intiequals1 REPO=virtual-user-ai PROJECT_NUMBER=2 ./scripts/setup_github_project2.sh
# Requirements:
#   - gh installed and authenticated
#   - access to the repository and user project

OWNER="${OWNER:-intiequals1}"
REPO="${REPO:-virtual-user-ai}"
PROJECT_NUMBER="${PROJECT_NUMBER:-2}"

need() {
  command -v "$1" >/dev/null 2>&1 || {
    echo "Missing required command: $1" >&2
    exit 1
  }
}

need gh

if ! gh auth status >/dev/null 2>&1; then
  echo "GitHub CLI is not authenticated. Run: gh auth login" >&2
  exit 1
fi

REPO_REF="${OWNER}/${REPO}"
PROJECT_REF="https://github.com/users/${OWNER}/projects/${PROJECT_NUMBER}"

echo "Using repo: ${REPO_REF}"
echo "Using project: ${PROJECT_REF}"

echo "Ensuring labels exist..."
for label in "priority:P0" "priority:P1" "priority:P2" "type:import" "type:hygiene" "type:validation" "type:adapter" "status:planned"; do
  gh label create "$label" --repo "$REPO_REF" --color "1D76DB" --force >/dev/null
  echo "  - $label"
done

create_issue() {
  local title="$1"
  local body="$2"
  local labels="$3"
  local out
  out=$(gh issue create --repo "$REPO_REF" --title "$title" --body "$body" --label "$labels")
  echo "$out"
}

echo "Creating baseline issues..."
ISSUE_URLS=()

ISSUE_URLS+=("$(create_issue \
  "P0: Audit missing POC files under product/system/poc_with_triggers" \
  "Create a definitive inventory of missing files versus documented architecture.\n\nAcceptance criteria:\n- Inventory grouped by module (core/media/adapter/tests/host setup).\n- Missing-file list checked into docs or posted in issue." \
  "priority:P0,type:import,status:planned")")

ISSUE_URLS+=("$(create_issue \
  "P0: Import first safe POC batch with explicit placeholders" \
  "Import the first substantial runnable code batch and keep unsupported/credential-dependent behavior behind explicit placeholders.\n\nAcceptance criteria:\n- First substantial batch present in repo.\n- Placeholders clearly marked." \
  "priority:P0,type:import,status:planned")")

ISSUE_URLS+=("$(create_issue \
  "P1: Resolve test.txt artifact (remove or justify)" \
  "Resolve the hygiene artifact by removing test.txt or documenting why it must remain.\n\nAcceptance criteria:\n- test.txt removed OR justification documented." \
  "priority:P1,type:hygiene,status:planned")")

ISSUE_URLS+=("$(create_issue \
  "P1: Add/verify smoke tests and align CI with real paths" \
  "Ensure smoke tests are present in-repo and CI references existing paths only.\n\nAcceptance criteria:\n- Smoke tests are runnable.\n- CI compile/smoke checks pass on real paths." \
  "priority:P1,type:validation,status:planned")")

ISSUE_URLS+=("$(create_issue \
  "P2: Continue Webex adapter in small, controlled increments" \
  "Continue Webex work only after import/hygiene/validation gates. Preserve dry-run support and shared-core boundaries.\n\nAcceptance criteria:\n- Dry-run remains functional.\n- send_audio path uses media worker contract." \
  "priority:P2,type:adapter,status:planned")")

echo "Adding issues to project..."
for url in "${ISSUE_URLS[@]}"; do
  gh project item-add "$PROJECT_NUMBER" --owner "$OWNER" --url "$url" >/dev/null
  echo "  - added $url"
done

echo "Done. Created and added ${#ISSUE_URLS[@]} issues to ${PROJECT_REF}."
