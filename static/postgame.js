class PostGame {
    constructor() {
        this.$createBtn = $("#create-btn");
        this.$leaderboardDiv = $("#leaderboard");
        this.$memeInfoDiv = $("#meme-info");
        this.initEventListeners();
        this.fetchGameRecord();
        this.fetchAllGameRecords();
      }
  
    initEventListeners() {
      this.$createBtn.on("click", this.createMeme.bind(this));
    }
  
    createMeme() {
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
        const container = $(".gameover-img");
        container.empty();
        console.log(response);
        if (response.success) {
          const url = response.data.url;
          const img = $("<img>").attr("src", url);
          const favoriteIcon = $("<i class='fas fa-star favorite-icon'></i>");
          container.append(img, favoriteIcon);
  
          favoriteIcon.on("click", function () {
            $(this).toggleClass("active");
            // Save the favorite status in your API/database here
          });
        } else {
          const errorMessage = response.error_message || "Unknown error";
          container.append($("<p>").text(`Error: ${errorMessage}`));
        }
      }
    }
  
    renderLeaderboard(leaderboardData) {
      let leaderboardHTML = "<h2>Leaderboard</h2><ul>";
  
      leaderboardData.forEach((entry) => {
        leaderboardHTML += `<li>${entry.username} - ${entry.total_score} points</li>`;
      });
  
      leaderboardHTML += "</ul>";
      this.$leaderboardDiv.html(leaderboardHTML);
    }
  
    renderMemeInfo(memeData) {
      const memeInfoHTML = `
        <h2>Meme Information</h2>
        <p>Phrase: ${memeData.phrase}</p>
        <p>Image URL: ${memeData.image_url}</p>
      `;
  
      this.$memeInfoDiv.html(memeInfoHTML);
    }
  
    getGameRecord() {
        axios
          .get('/app/game/get-game-record')
          .then((response) => {
            console.log('GameRecord:', response.data);
            this.displayGameRecord(response.data);
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      }
    
      displayGameRecord(data) {
        const round = data.round;
        const displayElement = document.getElementById('mostRecentGameRecord');
    
        if (round !== undefined) {
          displayElement.textContent = `Most recent game's round: ${round}`;
        } else {
          displayElement.textContent = 'No game records found';
        }
      }
    
      getAllGameRecords() {
        axios
          .get('/app/game/get-all-game-records')
          .then((response) => {
            console.log('Fetched GameRecords:', response.data);
            this.displayGameRecordChart(response.data);
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      }
    
      displayGameRecordChart(data) {
        const ctx = document.getElementById('gameRecordChart').getContext('2d');
    
        const labels = ['0', '1', '2', '3', '4'];
        const counts = labels.map((label) => data[label] || 0);
    
        new Chart(ctx, {
          type: 'bar',
          data: {
            labels: labels,
            datasets: [
              {
                label: 'Number of Games',
                data: counts,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1,
              },
            ],
          },
          options: {
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        });
      }

  }
  
  // Initialize the MemeGame class
  const postGame = new PostGame();
  
  // Example usage of renderLeaderboard and renderMemeInfo methods
  const leaderboardData = [
    { username: "user1", total_score: 100 },
    { username: "user2", total_score: 80 },
    { username: "user3", total_score: 60 },
  ];
  
  const memeData = {
    phrase: "This is a meme phrase",
    image_url: "https://example.com/meme-image.jpg",
  };
  
  postGame.renderLeaderboard(leaderboardData);
  postGame.renderMemeInfo(memeData);
  
