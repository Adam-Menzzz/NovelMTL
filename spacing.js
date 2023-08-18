document.addEventListener("DOMContentLoaded", function() {
  var paragraph = document.getElementById("chapter");
  var textContent = paragraph.textContent;
  var newText = textContent.replace(/\n/g, '<br>'); // Replace new lines with line breaks
  paragraph.innerHTML = newText;
});