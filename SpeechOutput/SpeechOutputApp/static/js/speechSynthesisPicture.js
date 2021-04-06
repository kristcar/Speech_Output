if ("speechSynthesis" in window) {
  const synth = window.speechSynthesis;
  var flag = false;

  //***************Voices***************
  const voiceSelect = document.querySelector("#voice-select");

  let voices = [];

  const getVoices = () => {
    voices = synth.getVoices();

    // Loop through voices and create an option for each one
    voices.forEach((voice) => {
      // Create option element
      const option = document.createElement("option");
      // Fill option with voice and language
      option.textContent = voice.name + "(" + voice.lang + ")";

      // Set needed option attributes
      option.setAttribute("data-lang", voice.lang);
      option.setAttribute("data-name", voice.name);
      voiceSelect.appendChild(option);
    });
  };

  getVoices();
  if (synth.onvoiceschanged !== undefined) {
    synth.onvoiceschanged = getVoices;
  }
  // ***************End Voices***************

  /* references to the buttons */
  var playEle = document.querySelector("#play");

  /* click event handlers for the buttons */
  playEle.addEventListener("click", onClickPlay);

  function onClickPlay() {
    if (!flag) {
      flag = true;
      utterance = new SpeechSynthesisUtterance(
        document.querySelector(".speech_item").textContent
      );

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
}
