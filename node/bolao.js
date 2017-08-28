let seqs = [];

if (process.argv[2] == '--help' || !process.argv[2]){
	console.log('node jogo.js (Num Jogadores) (Qtd Numeros) (Amplitude de numeros[1-x]) (Numero de jogos por jogador)');
	return;
}

if (process.argv.length != 6) {
	console.log('Falta parametros');
	return;
}

let numJogadores = Number(process.argv[2]);
let qtdNumeros = Number(process.argv[3]);
let amplitude = Number(process.argv[4]);
let jogosPorJogador = Number(process.argv[5]);


for (let w=1; w<= numJogadores; w++){
	console.log('Jogador '+w);
	for (let x=1; x<= jogosPorJogador; x++){
		getSeq();
	}
	console.log('');
	console.log('');
}


function getSeq() {
	let numbers = [];
	for (let i=1; i<=qtdNumeros; i++) {
		Math.random();
		Math.random();
		let num = Math.floor(Math.random() * amplitude + 1);
		
		if(!alreadyChosen(numbers,num))
			numbers.push(num);
		else
			i--;

		// console.log(num, i);
	}

	numbers.sort((a,b) => (a - b));

	if (!isSeqNew(numbers))
		getSeq();

	seqs.push(numbers);
	console.log(numbers);
}

function alreadyChosen(numbers,num) {
	for (let idx in numbers) {
		if (numbers[idx] == num){
			return true;
		}
	}
	return false;
}

function isSeqNew (seq) {
	for (let idx in seqs) {
		if (seqs[idx] == seq) 
			return false;
	}
	return true;
}


