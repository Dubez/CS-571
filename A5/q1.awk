#awk script to make sure that each line has the same number of scores
BEGIN{max = 0}
{
	count[$1] = NF-1
}
END{
	for(name in count){
		if(count[name]>max){
			max = count[name]
		}
	}
	for(name in count){
		if(count[name] < max){
			print name, "is missing", (max - count[name]), "scores"
		}
	}
	print "No missing scores"
}
		
