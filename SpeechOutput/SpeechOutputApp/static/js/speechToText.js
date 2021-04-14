var speechRecognition = window.webkitSpeechRecognition;
var recognition = new speechRecognition();
recognition.continuous = true;

var instructions = $("#instructions");
var generated_text = $("#generated_text");
var content = "";

recognition.onstart = function () {
  instructions.text("Voice Recognition is on!");
};

recognition.onspeechend = function () {
  instructions.text("Voice Recognition is off.");
};

recognition.onerror = function () {
  instructions.text("Cannot detect voice, please try again.");
};

recognition.onresult = function (event) {
  var current = event.resultIndex;
  var transcript = event.results[current][0].transcript; //spoken data
  content += transcript;
  generated_text.val(content);
};

$("#start_button").click(function (event) {
  if (content.length) {
    content += "";
  }
  recognition.start();
});

generated_text.on("input", function () {
  content = $(this).val();
});
