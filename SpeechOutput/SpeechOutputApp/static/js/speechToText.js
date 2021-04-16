window.SpeechRecognition =
  window.SpeechRecognition || window.webkitSpeechRecognition;

const recognition = new SpeechRecognition();
recognition.interimResults = true;
recognition.lang = "en-US";

let p = document.createElement("p");
const words = document.querySelector(".speech_output");
words.appendChild(p);

recognition.addEventListener("result", (e) => {
  const transcript = Array.from(e.results)
    .map((result) => result[0])
    .map((result) => result.transcript)
    .join("");

  const smileScript = transcript.replace(/smile emoji/gi, "😊");
  p.textContent = smileScript;

  if (e.results[0].isFinal) {
    p = document.createElement("p");
    words.appendChild(p);
  }
});

recognition.addEventListener("end", recognition.start);

recognition.start();

// $("#start").on("click", function (e) {
//   recognition.start();
// });

// $("#stop").on("click", function (e) {
//   recognition.stop();
// });

// $().alert("close");
