#!/bin/bash
# chdir input
# for i in *.txt
# do
#     echo "running test $i"
#     python ../quibble.py curevents.txt ../outputs/$i.txt < $i.txt > ../outputs/$i.log
# done

rm outputs/*

COUNTER=1
while [  $COUNTER -lt 81 ]; do  # loop through 80 test cases
    python ../quibble.py input_files/test_"$COUNTER"_input_file.txt outputs/test_"$COUNTER"_actual_output_file.txt < input/test_"$COUNTER"_input.txt > outputs/test_"$COUNTER"_actual_output.txt
    let COUNTER=COUNTER+1
done


rm -f test_results.txt

COUNTER=1
while [  $COUNTER -lt 81 ]; do  # validate 80 tests
    echo "" >> test_results.txt
    echo "==== Test Case $COUNTER ====" >> test_results.txt

    if diff --ignore-all-space --ignore-case outputs/test_"$COUNTER"_actual_output_file.txt expected_output_files/test_"$COUNTER"_output_file.txt >> test_results.txt ;
    then
        echo "Output File Test Passed" >> test_results.txt
    fi

    if diff --ignore-all-space --ignore-case outputs/test_"$COUNTER"_actual_output.txt expected_output/test_"$COUNTER"_output.txt >> test_results.txt ;
    then
        echo "Output Test Passed" >> test_results.txt
    fi

    echo "======================" >> test_results.txt

    let COUNTER=COUNTER+1
done
