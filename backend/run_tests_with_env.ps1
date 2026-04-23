# Windows PowerShell
$env:LANGCHAIN_CALLBACKS_DISABLED="true"
pytest %*

# Bash (Linux/macOS)
# export LANGCHAIN_CALLBACKS_DISABLED=true
# pytest "$@"
