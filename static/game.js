class MemeoGame {
  constructor(boardId, imageSrc) {
    this.board = $("#" + boardId);
    this.round = 1;
    this.result = "";
    this.imageSrc = imageSrc;
    this.addImage(this.imageSrc);
    this.addTiles(this.round);
    this.showRound(this.round, this.result);

    $(".add-keyword", this.board).on("submit", this.handleSubmit.bind(this));
  }

  renderMessage(message, className) {
    const container = $(".msg", this.board);
    container.empty();
    const msg = $("<p>").text(message);
    container.addClass(className);
    container.append(msg);
  }

  renderPhraseMessage(phrase) {
    const container = $(".msg", this.board);
    const phraseMsg = $("<p>").text(`The phrase was: ${phrase}`);
    container.append(phraseMsg);
  }

  showMessage(message, result, phrase = null) {
    if (result === "not-correct") {
      this.renderMessage(message, "error");
    } else if (result === "game-over") {
      this.renderMessage(message, "danger");
      this.renderPhraseMessage(phrase);
    } else if (result === "correct") {
      this.renderMessage(message, "success");
      this.renderPhraseMessage(phrase);
    } else {
      this.renderMessage(message, "danger");
    }
  }
    
    addImage(src) {
        const container = $(".image-container", this.board);
        const image = $("<img>").attr("src", src);
        container.empty()
        container.append(image);
    }

    removeTiles() {
      const container = $(".tiles-container", this.board);
      container.empty();
    }

    showRound(round, result) {
      const totalLetters = 5;
      if (result === "correct") {
        for (let i = 1; i <= totalLetters; i++) {
          const letter = $(`#letter-${i}`);
          letter.removeClass("red");
          letter.addClass("green");
        }
      } else if (result === "not-correct") {
        const letter = $(`#letter-${round}`);
        letter.addClass("red");
      }
    }

    addTiles(round) {
        const numRows = 4;
        const numCols = 4;
        const container = $(".tiles-container", this.board);
        container.empty();
      
        let numVisibleTiles = 1;
        for (let i = 1; i <= round; i++) {
          numVisibleTiles += (i * 2) - 1;
        }
      
        // Generate shuffled list of tile indices
        const tileIndices = [...Array(numCols * numRows).keys()];
        shuffle(tileIndices);
      
        // Assign visibility status based on shuffled list
        for (let i = 0; i < numRows; i++) {
          for (let j = 0; j < numCols; j++) {
            const tile = $("<div>").addClass("tile");
            const tileIndex = i * numCols + j;
            if (tileIndices.indexOf(tileIndex) < numVisibleTiles) {
              tile.addClass("visible");
            } else {
              tile.addClass("hidden");
            }
            container.append(tile);
          }
        }
      }
      

      async handleSubmit(evt) {
        console.log("handleSubmit called");
        console.log(this.round)
        evt.preventDefault();
        const inputField = $(".keyword");
        const keyword = inputField.val();
        inputField.val("");
    
        const response = await axios.get("/update-game-meme", {
            params: { keyword: keyword },
        });
    
        console.log("Response data: ", response.data);

        const { result, message, phrase } = response.data;
    
        if (result === "not-correct") {
            console.log("handleSubmit - not correct called")
            this.round++;
            this.addTiles(this.round);
            this.showRound(this.round, result);
            this.showMessage(message, result, phrase);
            console.log(this.round)
        } else if (result === "correct") {
            console.log("handleSubmit - correct called")
            this.round++;
            this.removeTiles();
            this.addImage(this.imageSrc);
            this.showRound(this.round, result);
            this.showMessage(message, result, phrase);
            console.log(this.round)
            setTimeout(() => {
              window.location.href = "/game-over";
          }, 10000);
        } else if (result === "game-over") {
          console.log("handleSubmit - game over called")
            this.showRound(this.round, result);
            this.removeTiles();
            this.addImage(this.imageSrc);
            this.showRound(this.round, result);
            this.showMessage(message, result, phrase);
            console.log(this.round)
            setTimeout(() => {
              window.location.href = "/game-over";
          }, 10000);
        }
    }
}

function shuffle(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
}