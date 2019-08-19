# script to find the middle grade in the class
# it takes its input from q5a.awk as follows: awk -f q5a.awk scores | sort -n +1 -2 | awk -f q5b.awk

{
	student[NR] = $1
	avg[NR] = $2
}

END{
		
	printf "The middle score in the class is the %dth grade: %d and it belongs to: %s\n",(int(NR/2)+1), avg[(int(NR/2)+1)],student[(int(NR/2)+1)] 
		
	
}

