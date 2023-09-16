const emojiButton = document.getElementById("emoji-button");
const emojiContainer = document.getElementById("emoji-container");

emojiButton.addEventListener("click", () => {
  fetch("https://random-emoji-api.herokuapp.com/emoji")
    .then((response) => response.json())
    .then((data) => {
      const randomEmoji = data.emoji;
      emojiContainer.textContent = randomEmoji;
    })
    .catch((error) => {
      console.error("Error al obtener emoji:", error);
    });
});