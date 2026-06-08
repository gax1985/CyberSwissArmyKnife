# justfile for Cyber Swiss Army Knife

# Default recipe to list all available commands
default:
    @just --list

# Trigger the Langflow API pipeline with a specific flow ID and document path
trigger-flow flow_id document_path:
    python trigger_langflow.py {{flow_id}} {{document_path}}

# Check if Ollama is running locally
check-ollama:
    curl -I http://localhost:11434/

# Check if Langflow is running locally
check-langflow:
    curl -I http://localhost:7860/

# Verify Git status
git-status:
    git status

# Check the authentication status of the GitHub CLI
gh-status:
    gh auth status

# Print commands run by the Gemini agent during repository setup
agent-setup-history:
    @echo "=========================================================="
    @echo " Commands run by Gemini Agent during repository setup:    "
    @echo "=========================================================="
    @echo " 1. git status; git remote -v; gh --version"
    @echo " 2. git config --global --add safe.directory D:/Projects/CyberSwissArmyKnife/CyberSwissArmyKnife"
    @echo " 3. git status; git remote -v"
    @echo " 4. gh --version"
    @echo " 5. $env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [System.Environment]::GetEnvironmentVariable('Path','User'); gh --version"
    @echo " 6. $env:Path = [System.Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [System.Environment]::GetEnvironmentVariable('Path','User'); gh auth status"
    @echo " 7. git reset; git add .; git commit -m 'initial commit: project structure and core langflow client'"
    @echo " 8. git add .; git commit -m 'docs: add justfile, update AI instructions, and record agent execution history'"
    @echo " 9. Get-ChildItem ~\\.ssh"
    @echo " 10. ssh -T git@github.com; git push -u origin master"
    @echo " 11. Test-Path \$env:APPDATA\\Claude\\claude_desktop_config.json; Get-ChildItem -Path \$env:APPDATA -Filter *mcp*config* -Recurse -ErrorAction SilentlyContinue"
    @echo " 12. Get-Content \$env:APPDATA\\Claude\\claude_desktop_config.json"
    @echo " 13. Test-Path \$HOME\\.continue\\config.json; Test-Path \$env:APPDATA\\VSCodium\\User\\globalStorage\\continue.continue\\config.json; ..."
    @echo " 14. git add -f .gemini/settings.json; git status"
    @echo " 15. New-Item -ItemType Directory -Force -Path C:\\Users\\gax19\\.gemini\\antigravity; Copy-Item ..."
    @echo " 16. Get-Content C:\\Users\\gax19\\.gemini\\antigravity\\mcp_config.json"
