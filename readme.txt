1. Karyotype file with chromosome sizes
I renamed your chromosomes to OsChrX, X={1..12,Un,Sy} and DrChr_Y, Y = {1..21},
since the original names are too long to be shown properly.
I then generated the Karyotype file from your two chr_sizes files.
The last column determines the colour of the chromosome, you'll have to play with that.

2. Link data file. I generated this from your synteny table using my blast2links.py script.
(takes the file as input and optional a --min-pid parameter that determines the cutoff for the percent identity value,
the default is 75%, i.e. --min-pid 0.75)

3. General config xml. I just took ours, stripped it of all SNP data and added the <links> section
according to the Circos tutorial.
