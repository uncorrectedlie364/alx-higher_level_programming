@!/usr/bin/node

const arg = process.argv[2];
const count = Number(arg);

if (isNaN(count) || count <= 0) {
	console.log('Missing number of occurences');
} else {
	for (let i = 0, i < count; i++) {
		console.log('C is fun');
	}
}
