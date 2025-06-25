<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Barışalım mı Aras Grayson Style?</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@600&display=swap');
  body {
    margin: 0; 
    background: linear-gradient(135deg, #121212 0%, #1f1f2e 100%);
    color: #00ffa2;
    font-family: 'Montserrat', sans-serif;
    display: flex; 
    flex-direction: column;
    justify-content: center; 
    align-items: center;
    height: 100vh;
    overflow: hidden;
    text-align: center;
    padding: 20px;
  }
  h1 {
    font-size: 2.8rem;
    margin-bottom: 10px;
    text-shadow: 0 0 12px #00ffa2;
  }
  p {
    font-size: 1.2rem;
    margin-bottom: 30px;
    color: #a0ffa2cc;
  }
  .buttons {
    display: flex;
    gap: 30px;
    justify-content: center;
  }
  button {
    padding: 15px 35px;
    font-size: 1.2rem;
    border: none;
    border-radius: 10px;
    cursor: pointer;
    font-weight: 600;
    box-shadow: 0 0 10px #00ffa2cc;
    transition: transform 0.3s ease;
    user-select: none;
  }
  #yesBtn {
    background: #00ffa2;
    color: #000;
  }
  #noBtn {
    background: #ff004c;
    color: #fff;
    position: relative;
  }
  #noBtn.scared {
    animation: shake 0.3s ease infinite alternate;
  }
  @keyframes shake {
    0% { transform: translateX(0); }
    100% { transform: translateX(6px); }
  }
  #message {
    margin-top: 40px;
    font-size: 1.6rem;
    color: #00ffa2;
    text-shadow: 0 0 12px #00ffa2;
  }
  /* Konfeti */
  .confetti-piece {
    position: fixed;
    width: 10px;
    height: 10px;
    background-color: #00ffa2;
    opacity: 0.8;
    top: 0;
    animation-name: fall;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
  }
  @keyframes fall {
    0% {
      transform: translateY(0) rotate(0deg);
      opacity: 1;
    }
    100% {
      transform: translateY(100vh) rotate(360deg);
      opacity: 0;
    }
  }
  /* "Kafanı küçültüyorum" animasyon */
  #shrinkMessage {
    position: fixed;
    top: 20px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 2.2rem;
    color: #ff004c;
    font-weight: 700;
    text-shadow: 0 0 12px #ff004c;
    opacity: 0;
    transition: opacity 0.5s ease;
  }
  #shrinkMessage.show {
    opacity: 1;
  }
  /* Tokalaşan adam GIF */
  #handshake {
    margin-top: 25px;
    max-width: 150px;
    display: none;
    filter: drop-shadow(0 0 5px #00ffa2);
  }
  /* Footer */
  footer {
    margin-top: 50px;
    font-size: 0.9rem;
    color: #555;
    font-style: italic;
  }
</style>
</head>
<body>

<h1>Kanka, aramızda bi’ şey varsa bi’ çözelim artık!</h1>
<p>Dalga geçtim, kırmak istemedim. Ama barışmazsan kafan küçülür, uyarıyorum! 😜</p>

<div class="buttons">
  <button id="yesBtn">Evet, barıştık 🤜🤛</button>
  <button id="noBtn">Hayır, kafam küçülmesin 😤</button>
</div>

<div id="message"></div>
<img id="handshake" src="https://i.imgur.com/3XHnNIN.gif" alt="Tokalaşma GIF'i" />

<div id="shrinkMessage">Kafanı küçültüyorum ulan! 😡</div>

<footer>by Aras Grayson 🦞 – Dalga geçmek bizim işimiz, kırmak değil.</footer>

<script>
  const yesBtn = document.getElementById('yesBtn');
  const noBtn = document.getElementById('noBtn');
  const message = document.getElementById('message');
  const shrinkMessage = document.getElementById('shrinkMessage');
  const handshake = document.getElementById('handshake');
  let noClickCount = 0;

  function createConfetti() {
    for(let i = 0; i < 30; i++) {
      const confetti = document.createElement('div');
      confetti.classList.add('confetti-piece');
      confetti.style.left = Math.random() * window.innerWidth + 'px';
      confetti.style.animationDuration = (3 + Math.random() * 3) + 's';
      confetti.style.animationDelay = Math.random() * 5 + 's';
      document.body.appendChild(confetti);
      setTimeout(() => confetti.remove(), 6000);
    }
  }

  yesBtn.addEventListener('click', () => {
    message.textContent = 'Aha tamam, ben de seni seviyorum lan kardeşim benim ❤️';
    handshake.style.display = 'block';
    createConfetti();
    noBtn.disabled = true;
    yesBtn.disabled = true;
  });

  noBtn.addEventListener('click', () => {
    noClickCount++;
    noBtn.classList.add('scared');
    noBtn.style.transform = `scale(${1 - noClickCount * 0.15})`;
    if(noClickCount >= 5) {
      shrinkMessage.classList.add('show');
      noBtn.disabled = true;
    }
    setTimeout(() => {
      noBtn.classList.remove('scared');
    }, 500);
  });
</script>

</body>
</html>