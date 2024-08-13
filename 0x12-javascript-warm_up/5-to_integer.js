#!/usr/bin/node

const argument = process.argv[2];
const number = Number(argument);

if (!isNAn(number)) {
	console.log('My number: ${Math.floor(number)}');
} else {
	console.log('Not a number');
}
