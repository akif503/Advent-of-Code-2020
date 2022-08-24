const read = require('./read');

const input = read('4.txt').split('\n\n')
                        .map(line => [...[...line.matchAll(/\w{3}:/g)].join('')].sort().join(''))
                        .filter(line => line == '::::::::bcccddeeghhiiillprrrtyyy' 
                                        || line == ':::::::bccdeeghhiillprrrtyyy');

const answer = input.length;
console.log(answer);

/*
    Split on double line breaks

    Take each line and

    Find all matches of three "word" characters, followed by a colon (let matches = line.matchAll(/\w{3}:/g))

    Spread that iterator out into a new array, and join it with an empty string (let str = [...matches].join(''))

    Convert that string into a character array ([...str]. Alternatively, str.split(''))

    Sort those letters alphabetically and join them back into a string (.sort().join(''))

    Filter out the ones that have all the letters (optionally including cid: in the mix).

    Count the length
*/