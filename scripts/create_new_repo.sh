#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "Usage: $0 <repo-name> [target-directory]" >&2
  exit 1
fi

repo_name="$1"
target_dir="${2:-.}"
repo_path="${target_dir%/}/${repo_name}"

if [[ -e "$repo_path" ]]; then
  echo "Error: path already exists: $repo_path" >&2
  exit 1
fi

mkdir -p "$repo_path"
cd "$repo_path"

git init -b main >/dev/null
cat > README.md <<EOT
# ${repo_name}

Dieses Repository wurde mit \`scripts/create_new_repo.sh\` erstellt.
EOT

cat > .gitignore <<'EOT'
# Python
__pycache__/
*.py[cod]

# Environment
.env
.venv/

# OS
.DS_Store
Thumbs.db
EOT

git add README.md .gitignore
git commit -m "Initial commit" >/dev/null

echo "Neues Repository erstellt: $repo_path"
