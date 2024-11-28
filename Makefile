all: serve

extract:
	rm -rf sources/uyv/analytics.duckdb
	cd extract && uv run extraction.py

serve:
	npm run sources && npm exec evidence dev -- --host 0.0.0.0 --open /

fclean:
	rm sources/uyv/analytics.duckdb

re: fclean all

.PHONY: extract serve fclean re