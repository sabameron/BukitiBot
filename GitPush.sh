#!/bin/bash

current_date=$(date +%Y-%m-%d)
current_time=$(date +%H-%M-%S)

commit_message="AutomaticPush_${current_date}_${current_time}"

git status
git add .
git commit -m "$commit_message"
sleep 2
git push origin master