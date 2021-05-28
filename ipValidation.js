function isValidIP(str) {
    valid = 0, dots = 0, pattern = /[0-9]/g, octets = str.split(".");
    for(i = 0; i < str.length; i++){
        if(str[i] == ".") dots += 1;
        if(octets[i] >= 0 && octets[i] <= 255) valid += 1;
    }
    return (valid == 4 && dots == 3) ? true : false;
}