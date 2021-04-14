var speechRecognition = window.webkitSpeechRecognition;
var recognition = new speechRecognition();

var instructions = $("instructions");
var generated_text = $("#generated_text");
var content = "";
