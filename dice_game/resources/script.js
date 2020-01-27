/*
GAME RULES:

- The game has 2 players, playing in rounds
- In each turn, a player rolls a dice as many times as he whishes. Each result get added to his ROUND score
- BUT, if the player rolls a 1, all his ROUND score gets lost. After that, it's the next player's turn
- The player can choose to 'Hold', which means that his ROUND score gets added to his GLBAL score. After that, it's the next player's turn
- The first player to reach 100 points on GLOBAL score wins the game

*/

var dice,
  diceOne,
  numOne,
  diceDOM = document.querySelector(".dice"),
  diceOneDOM = document.querySelector(".dice-1"),
  roundScore,
  activePlayer,
  score,
  gamePlaying,
  sixes,
  num,
  limit;

init();

document.querySelector(".btn-roll").addEventListener("click", function() {
  if (gamePlaying) {
    dice = roll();
    if (dice[0] === 1 && dice[1] === 1) {
      addScore(dice[0], dice[1]);
    } else if (dice[0] === 1 || dice[1] === 1) {
      nextPlayer();
    } else {
      addScore(dice[0], dice[1]);
    }
  }
});

document.querySelector(".btn-hold").addEventListener("click", function() {
  if (gamePlaying) {
    score[activePlayer] += roundScore;
    document.querySelector("#score-" + activePlayer).textContent =
      score[activePlayer];
    if (score[activePlayer] >= limit) {
      document.querySelector("#name-" + activePlayer).textContent = "Winner";
      diceDOM.style.display = "none";
      diceOneDOM.style.display = "none";
      document
        .querySelector(".player-" + activePlayer + "-panel")
        .classList.add("winner");
      document
        .querySelector(".player-" + activePlayer + "-panel")
        .classList.remove("active");
      gamePlaying = false;
    } else {
      nextPlayer();
    }
  }
});

document.querySelector(".btn-new").addEventListener("click", init);
function nextPlayer() {
  activePlayer === 0 ? (activePlayer = 1) : (activePlayer = 0);
  roundScore = 0;
  document.getElementById("current-0").textContent = "0";
  document.getElementById("current-1").textContent = "0";
  document.querySelector(".player-0-panel").classList.toggle("active");
  document.querySelector(".player-1-panel").classList.toggle("active");
  diceDOM.style.display = "none";
  diceOneDOM.style.display = "none";
}
function init() {
  (roundScore = 0), (activePlayer = 0), (score = [0, 0]), (gamePlaying = true);
  limit = prompt("Enter desired limit");
  diceDOM.style.display = "none";
  diceOneDOM.style.display = "none";
  document.getElementById("score-0").textContent = "0";
  document.getElementById("score-1").textContent = "0";
  document.getElementById("current-0").textContent = "0";
  document.getElementById("current-1").textContent = "0";
  document.querySelector("#name-0").textContent = "Player-1";
  document.querySelector("#name-1").textContent = "Player-2";
  document.querySelector(".player-0-panel").classList.remove("winner");
  document.querySelector(".player-1-panel").classList.remove("winner");
  document.querySelector(".player-0-panel").classList.remove("active");
  document.querySelector(".player-0-panel").classList.add("active");
  document.querySelector(".player-1-panel").classList.remove("active");
}
function roll() {
  num = Math.floor(Math.random() * 6) + 1;
  numOne = Math.floor(Math.random() * 6) + 1;
  diceDOM.style.display = "block";
  diceOneDOM.style.display = "block";
  diceDOM.src = "/resources/img/dice-" + num + ".png";
  diceOneDOM.src = "/resources/img/dice-" + numOne + ".png";
  if (num === 6 && numOne === 6) {
    score[activePlayer] = 0;
    document.getElementById("score-" + activePlayer).textContent = "0";
    alert("Double Sixes Player -" + (activePlayer + 1));
    return [1, 4];
  }
  return [num, numOne];
}

function addScore(dice, diceOne) {
  roundScore += dice + diceOne;
  document.querySelector("#current-" + activePlayer).textContent = roundScore;
}
