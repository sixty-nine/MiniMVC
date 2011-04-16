#!/bin/sh
rm doc/*
epydoc -o doc/ --graph all src/lib/MiniMVC

