Write-Host "Running Ruff check..."
uv run --project apps/api ruff check . --fix

Write-Host "Running Ruff format..."
uv run --project apps/api ruff format .

Write-Host "Running tests..."
uv run --project apps/api pytest tests

Write-Host "Running dependency audit..."
uv run --project apps/api pip-audit