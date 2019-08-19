# awk script to count number of As, Bs,...
# used as follows from the terminal: awk -f q6.awk scores | awk -f q7.awk

{
	
	cumm[$2]++
}

END{
	for(i in cumm){
		printf "The number of %s's is: %d\n",i,cumm[i]
		
	}
	
}
