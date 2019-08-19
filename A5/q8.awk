#awk script to generate a histogram based on students' grades
# this script takes as input, the output of question 6
# used as follows from the terminal: awk -f q6.awk scores | awk -f q8.awk


{
	
	cumm[$2] = cumm[$2] "*"
}

END{
	for(i in cumm){
		printf "%s: %s\n",i,cumm[i]
		
	}
	
}


