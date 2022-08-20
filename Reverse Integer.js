var reverse = function(x) {
    var num = Math.abs(x);
    var flag = 1;
    var answer = 0, reminder = 0;

    if ( x < 0 ) {
        flag = -1;
    }

	while( num > 0 ) {
		reminder = num % 10;
		answer = answer*10 + reminder;
        num = (num - reminder) / 10;
	}

	if ( answer >= Math.pow(2,31) ) {
        return 0;
    }

    return answer*flag;
};