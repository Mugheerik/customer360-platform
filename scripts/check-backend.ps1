Write-Host "Running Ruff check..."
uv run ruff check . --fix

Write-Host "Running Ruff format..."
uv run ruff format .

Write-Host "Running tests..."
uv run pytest ../../tests

Write-Host "Running dependency audit..."
uv run pip-audit