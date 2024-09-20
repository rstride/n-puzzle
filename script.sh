(
head -n 1 temp_puzzle.txt;
size=$(head -n 2 temp_puzzle.txt | tail -n 1 | tr -d -c 0-9);
tail -n +3 temp_puzzle.txt | xargs -n$size | awk -v size="$size" '{
    for (i=1; i<=size; i++)
        a[NR,i] = $i
}
END {
    for (i=1; i<=size; i++) {
        for (j=1; j<=NR; j++)
            printf a[j,i] " "
        print ""
    }
}') > formatted_puzzle.txt
