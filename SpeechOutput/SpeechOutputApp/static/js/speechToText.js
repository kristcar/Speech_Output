//Utilizing the Web Speech API

//Browser identifier
// Firefox 1.0+
var isFirefox = typeof InstallTrigger !== "undefined";

// Chrome 1+
var isChrome = !!window.chrome && !!window.chrome.webstore;

if ("webkitSpeechRecognition" in window) {
  let recognition = new webkitSpeechRecognition();

  let final_transcript = "";

  recognition.continuous = true;
  recognition.interimResults = true;
  recognition.lang = "en-US";

  recognition.onstart = () => {
    document.querySelector("#status").style.display = "block";
  };
  recognition.onerror = () => {
    document.querySelector("#status").style.display = "none";
  };
  recognition.onend = () => {
    document.querySelector("#status").style.display = "none";
  };

  recognition.onresult = (event) => {
    let interim_transcript = "";

    for (let i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        final_transcript += " " + event.results[i][0].transcript;
      } else {
        interim_transcript += " " + event.results[i][0].transcript;
      }
    }

    //Add transcript to HTML
    document.querySelector("#final").innerHTML = final_transcript;
    document.querySelector("#interim").innerHTML = interim_transcript;
  };

  // Start and Stop Listening Buttons
  document.querySelector("#start").onclick = () => {
    recognition.start();
  };
  document.querySelector("#stop").onclick = () => {
    recognition.stop();
  };
} else {
  console.log("Speech Recognition Not Available");
}
