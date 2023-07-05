#!/bin/bash
echo "Hello World"
echo "ANDREAS Sucky sucky"

echo "Alexis is a golden retriever"

Alexis="dog"
echo "Alexis is a $Alexis"

#Alexis="cat"


if [[ $Alexis == "dog" ]]; then
    echo "Alexis is a dog"
elif [[ ! $Alexis == "dog" ]]; then
    echo "Is not a dog"
fi

# String evaluation 
Mydog_name="Khan"
Mydog_age="1"
Mydog_race="Bernen sennen"

test_string="My dog is a Bernen sennen and he is 1 years old and his name is Khan"
Mydog_string="My dog is a $Mydog_race and he is $Mydog_age years old and his name is $Mydog_name"

echo $test_string
echo $Mydog_string

if [[ $test_string == $Mydog_string ]]; then
    echo "My strings are identical"
fi

# Build string with if statements


