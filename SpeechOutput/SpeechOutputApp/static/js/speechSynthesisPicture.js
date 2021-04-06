if ("speechSynthesis" in window) {
  var synth = speechSynthesis;
  var flag = false;

  /* references to the buttons */
  var playEle = document.querySelector("#play");
  var pauseEle = document.querySelector("#pause");
  var stopEle = document.querySelector("#stop");

  /* click event handlers for the buttons */
  playEle.addEventListener("click", onClickPlay);
  pauseEle.addEventListener("click", onClickPause);
  stopEle.addEventListener("click", onClickStop);

  function onClickPlay() {
    if (!flag) {
      flag = true;
      utterance = new SpeechSynthesisUtterance(
        document.querySelector(".speech_item").textContent
      );
      utterance.voice = synth.getVoices()[0];
      utterance.onend = function () {
        flag = false;
      };
      synth.speak(utterance);
    }
    if (synth.paused) {
      /* unpause/resume narration */
      synth.resume();
    }
  }
  function onClickPause() {
    if (synth.speaking && !synth.paused) {
      /* pause narration */
      synth.pause();
    }
  }
  function onClickStop() {
    if (synth.speaking) {
      /* stop narration */
      /* for safari */
      flag = false;
      synth.cancel();
    }
  }
}
Create;
