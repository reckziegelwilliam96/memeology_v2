$("#caption-btn").on("submit", async function (evt) {
  evt.preventDefault();
  const inputTop = $("input[name=top-text]");
  const inputBottom = $("input[name=bottom-text]");
  const keyTop = inputTop.val();
  const keyBottom = inputBottom.val();
  inputTop.val("");
  inputBottom.val("");
  console.log("keyTop: " + keyTop);
  console.log("keyBottom: " + keyBottom);

  try {
    const response = await axios.post("/api/caption-image", {
      topText: keyTop,
      bottomText: keyBottom,
    });

    appendMeme(response.data);
  } catch (error) {
    console.log(error);
  }
});

function appendMeme(response) {
  const container = $('.gameover-img')
  container.empty()
  console.log(response);
  if (response.success) {
   const url = response.data.url;
   const img = $("<img>").attr("src", url);
   container.append(img);
  } else {
    const errorMessage = response.error_message || 'Unknown error';
    container.append($('<p>').text(`Error: ${errorMessage}`));
  }
}