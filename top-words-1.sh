#!/usr/bin/env bash
curl -sl "https://www.gutenberg.org/files/11/11-0.txt" |tr '[:upper:]' '[:lower:]'| grep -oE "[a-z\']{2,}"| sort| grep -Fvwf stopwords| uniq -c | sort -nr| head -n10
