#!/bin/bash

# check if file name is provided
if [ "$#" -ne 1 ]; then
    echo "how to use: $0 <.java name>"
    exit 1
fi

# get file name and class name
FILE=$1
CLASS_NAME=$(basename "$FILE" .java)

# confile Java program
javac "$FILE"
if [ $? -ne 0]; then
    echo "compiling fail"
    exit 1
fi

# run Java program
java "$CLASS_NAME"


