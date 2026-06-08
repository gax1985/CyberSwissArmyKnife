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
