#!/bin/sh

function scrape() {
  cd scraper
  ../venv/bin/python run.py
  cd ..
}

function start_db() {
  cd database
  docker-compose up -d
  sleep 30
  cd ..
}

function stop_db() {
  cd database
  docker-compose down
  cd ..
}

start_db && scrape && stop_db
