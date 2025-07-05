SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c

URL = "https://raw.githubusercontent.com/tidyverse/dplyr/master/data-raw/starwars.csv"

.PHONY: all top10

data:
	mkdir $@

data/starwars.csv: data
	curl -sL $(URL) > $@

top10: data/starwars.csv
	grep Human $< |
	cut -d, -f1,2 |
	sort -t, -k2 -nr|
	head
