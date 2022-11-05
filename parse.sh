#!/bin/bash

grep -o '"loc": "[^"]*' $1 | grep -o '[^"]*$' | tee $2



