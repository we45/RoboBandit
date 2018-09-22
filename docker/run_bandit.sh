#! /bin/sh
if [ "$1" = "bandit" ]; then
    bandit -r /src/ -f json -o /results/bandit.json;true
elif [ "$1" = "safety" ]; then
    safety check -r /src/requirements.txt --full-report --json > /results/safety.json;true
else
    echo 'Unable to understand the input. Bye...'
fi