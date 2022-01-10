install:
	poetry install
brain-games:
	poetry run braim-games
buil:
	poetry build
publish:
	poetry publish --dry-run
package-install:
	python3 -m pip install --user dist/*.whl
make lint:
	poetry run flake8 brain_games
