class PostGame {
    constructor() {
        this.$createBtn = $("#create-btn");
        this.$leaderboardDiv = $("#leaderboard");
        this.$memeInfoDiv = $("#meme-info");
        this.initEventListeners();
        this.getGameRecord();
        this.getAllGameRecords();
      }
  
      initEventListeners() {
        $("#caption-btn").on("submit", this.createMeme.bind(this));
      }
    
      async createMeme(evt) {
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
          const response = await axios.post("/caption-image", {
            topText: keyTop,
            bottomText: keyBottom,
          });
    
          this.appendMeme(response.data);
        } catch (error) {
          console.log(error);
        }
      }
  
      appendMeme(response) {
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
            const isFavorite = favoriteIcon.hasClass("active");
            this.saveMeme(url, isFavorite);
          });
        } else {
          const errorMessage = response.error_message || "Unknown error";
          container.append($("<p>").text(`Error: ${errorMessage}`));
        }
      }

      async saveMeme(memeUrl, isFavorite) {
        try {
          const response = await axios.post('/save-meme', {
            url: memeUrl,
            favorite: isFavorite,
          });
    
          // Handle response (e.g., show a success message, update the UI, etc.)
          console.log(response);
        } catch (error) {
          console.error('Error:', error);
        }
      }

  
    renderLeaderboard(leaderboardData) {
      let leaderboardHTML = "<h2>Leaderboard</h2><ul>";
  
      leaderboardData.forEach((entry) => {
        leaderboardHTML += `<li>${entry.username} - ${entry.total_score} points</li>`;
      });
  
      leaderboardHTML += "</ul>";
      this.$leaderboardDiv.html(leaderboardHTML);
    };
  
    renderMemeInfo(memeData) {
      const memeInfoHTML = `
        <h2>Meme Information</h2>
        <p>Phrase: ${memeData.phrase}</p>
        <p>Image URL: ${memeData.image_url}</p>
      `;
  
      this.$memeInfoDiv.html(memeInfoHTML);
    }
  
    getGameRecord() {
      console.log("GET GAME RECORD called")
        axios
          .get('/get-game-record')
          .then((response) => {
            console.log('GameRecord:', response.data);
            this.displayGameRecord(response.data);
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      }
    
      displayGameRecord(data) {
        console.log("DISPLAY GAME RECORD called")
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
          .get('/get-all-game-records')
          .then((response) => {
            console.log('Fetched GameRecords:', response.data);
            const recordCounts = this.countGameRecords(response.data);
            this.displayGameRecordChart(recordCounts);
          })
          .catch((error) => {
            console.error('Error:', error);
          });
      }
      
      countGameRecords(records) {
        const counts = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0, '5': 0};
      
        for (const record of records) {
          const round = record.round;
          if (counts.hasOwnProperty(round)) {
            counts[round]++;
          }
        }
      
        return counts;
      }
    
      displayGameRecordChart(data) {
        const ctx = document.getElementById('gameRecordChart').getContext('2d');
    
        const labels = ['0', '1', '2', '3', '4', '5'];
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
            maintainAspectRatio: false,
            scales: {
              y: {
                beginAtZero: true,
              },
            },
          },
        });
      }
  };
  
