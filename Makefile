default:
	@echo "Usage: make clean"
	@echo "       make upload"

clean:
	rm -rf moc_prices_source.egg-info
	rm -rf moneyonchain_prices_source.egg-info
	rm -rf */__pycache__
	rm -rf */*/__pycache__
	rm -rf dist
	rm -rf build

upload:
	rm -rf dist
	python3 setup.py sdist
	twine upload dist/*