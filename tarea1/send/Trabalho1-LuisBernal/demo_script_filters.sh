mkdir results_gray

declare list_files=( baboon.png )
declare filters=( 1 2 3 4 5 6 7 8 9 10)

for i in "${!filters[@]}"
do
    for j in "${!list_files[@]}"

    do
    echo "${filters[$i]}" "${list_files[$j]}"
    python3 filter.py -k ${filters[$i]} -s "results_gray/h${filters[$i]}_${list_files[$j]}" ${list_files[$j]}

    done
done