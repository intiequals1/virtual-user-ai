import unittest
from pathlib import Path


class TestProject2SetupAssets(unittest.TestCase):
    def setUp(self):
        self.workflow = Path('.github/workflows/setup-project2.yml')
        self.script = Path('scripts/setup_github_project2.sh')
        self.docs = Path('docs/github-project-2-setup.md')

    def test_files_exist(self):
        self.assertTrue(self.workflow.exists(), 'workflow file missing')
        self.assertTrue(self.script.exists(), 'setup script missing')
        self.assertTrue(self.docs.exists(), 'setup docs missing')

    def test_workflow_contains_required_cloud_setup_hooks(self):
        text = self.workflow.read_text(encoding='utf-8')
        required_fragments = [
            'workflow_dispatch',
            'PROJECT_SETUP_TOKEN',
            'actions/github-script@v7',
            'addProjectV2ItemById',
            'project_number',
            'priority:P0',
            'P0: Audit missing POC files under product/system/poc_with_triggers',
        ]
        for fragment in required_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, text)

    def test_cli_script_contains_required_steps(self):
        text = self.script.read_text(encoding='utf-8')
        required_fragments = [
            'set -euo pipefail',
            'need gh',
            'gh auth status',
            'gh issue create',
            'gh project item-add',
            'priority:P0',
            'status:planned',
        ]
        for fragment in required_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, text)

    def test_docs_cover_cloud_setup_and_accessibility(self):
        text = self.docs.read_text(encoding='utf-8')
        required_fragments = [
            'Recommended path (no local setup)',
            'PROJECT_SETUP_TOKEN',
            'Make Project #2 accessible without sign-in',
            'Visibility',
            'Public',
            'Quick verification',
        ]
        for fragment in required_fragments:
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, text)


if __name__ == '__main__':
    unittest.main()
