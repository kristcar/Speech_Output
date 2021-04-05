const synth = window.speechSynthesis;

const voiceSelect = document.querySelector("#voice-select");
const textForm = document.querySelector("#form");
const textInput = document.querySelector("#text-input");

const speak = () => {
  //Verify if speaking
  if (synth.speaking) {
    console.error("Already speaking!");
    return;
  }
  //Retrieve text to speak
  if (textInput.value !== "") {
    const speakText = new SpeechSynthesisUtterance(textInput.value);

    //End speaking
    speakText.onend = (e) => {
      console.log("Finished speaking!");
    };

    speakText.onerror = (e) => {
      console.error("Error, try again.");
    };
  }

  //Set Voice
  const selectedVoice = voiceSelect.selectedOptions[0].getAttributeCount(
    "data-name"
  );

  voices.forEach((voice) => {
    if (voice.name === selectedVoice) {
      speakText.voice = voice;
    }
  });

  //Speak!
  synth.speak(speakText);
};

//Event Listeners:
textForm.addEventListener("submit", (e) => {
  e.preventDefault();
  speak();
  textInput.blur();
});
