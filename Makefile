all: extract serve

extract:
	rm -rf sources/uyv/analytics.parquet
	cd extract && uv run extraction.py

serve:
	npm run sources && npm run dev

fclean:
	rm sources/uyv/analytics.parquet

re: fclean all

.PHONY: extract serve fclean re