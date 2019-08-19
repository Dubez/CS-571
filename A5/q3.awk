# awk script to print the maximum grade on the last test
# it takes input from the bash script as follows: bash q3.sh < scores |awk -f  q3.awk

{ print $1, $NF; exit;
	}
