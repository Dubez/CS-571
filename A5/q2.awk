#script to print the name of any student that scores a zero


{
	for(i=2; i<(NF+1); i++){
		if($i == 0){
			print $1, "scored a 0 on a test"
			break
		}
	}
}
