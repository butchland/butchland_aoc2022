#! /bin/sh
day=$1
mkdir -p exercises/day$day
jinja -D day $day exercises/day-tmplt.qmd > exercises/day$day.qmd
jinja -D day $day butchland_aoc2022/code.j2 > butchland_aoc2022/day$day.py
jinja -D day $day tests/testcode.j2 > tests/test_day$day.py
echo "done init day $day"
