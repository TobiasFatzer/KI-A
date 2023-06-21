<script>
  import axios from "axios";
  import { ProgressLinear, MaterialApp, ProgressCircular } from 'svelte-materialify';


  let img;
  let files;
  let prediction = "";
  let huggingFaceLoading = false;
  let huggingFaceErrorMessage = "";
  let predictionObject = [];
    let winnerWinnerChickenDinner = "";
    let estimatedTime = 0;
  

  $: if (files) {
      // Note that `files` is of type `FileList`, not an Array:
      // https://developer.mozilla.org/en-US/docs/Web/API/FileList
      console.log(files);

      //Adds a onload for the image. The callback onload is called when the image is loaded.
      actionOnImageLoad();

      let reader = new FileReader();
      reader.onload = (e) => {
          img.src = e.target.result;
          console.log(e.target.result);
      };
      reader.readAsDataURL(files[0]);

      for (const file of files) {
          console.log(`${file.name}: ${file.size} bytes`);
      }
  }
  $: if (prediction) {
    predictionObject = JSON.parse(prediction);
}

  function actionOnImageLoad() {
      // Set up the image onload event
      img.onload = function () {
          // Create a new canvas
          var canvas = document.createElement("canvas");
          canvas.width = img.width;
          canvas.height = img.height;

          // Get the canvas 2D context
          var ctx = canvas.getContext("2d");

          // Draw the image onto the canvas, ignoring the alpha channel
          ctx.drawImage(img, 0, 0);

          canvas.toBlob((blob) => {
              predict(blob);
          }, "image/jpeg");
      };
  }

  function predict(data) {
      let url =
      "https://api-inference.huggingface.co/models/fatzetob/Ponti_Object_Classification";
      axios
          .post(
              url,
              data, //image data
              {
                  headers: {
                      Authorization:
                          "Bearer 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",
                  },
              }
          )
          .then((response) => {
              console.log(response.data);
              huggingFaceLoading = false;
              huggingFaceErrorMessage = "";
              prediction = JSON.stringify(response.data);
              winnerWinnerChickenDinner = response.data[0].label;
              img = null
          })
          .catch(function (error) {
              // error 503 Object { error: "Model kuhs/cats_classficiation is currently loading", estimated_time: 20 }1
              if (error.response.status === 503) {
                  //503 is service unavaiulable
                  huggingFaceLoading = true;
                  huggingFaceErrorMessage = error.response.data.error;
                  console.log(error.response.data);
                  console.log(error.response.status);
                  console.log(error.response.headers);
                  setTimeout(() => predict(data), (estimatedTime + 5) * 1000); // Retry after estimated time + 5 seconds

              } else if (error.request) {
                  // The request was made but no response was received
                  // `error.request` is an instance of XMLHttpRequest in the browser and an instance of
                  // http.ClientRequest in node.js
                  console.log(error.request);
              } else {
                  // Something happened in setting up the request that triggered an Error
                  console.log("Error", error.message);
              }
              console.log(error.config);
          });
  }
</script>

{#if huggingFaceLoading}
  <ProgressCircular size={70} width={7} indeterminate color="success" />
{/if}
<label for="file_upload">Upload a picture:</label>
<input
  accept="image/*"
  bind:files
  id="file_upload"
  name="file_upload"
  type="file"
/>
{#if predictionObject !== undefined && !huggingFaceLoading}
{#each predictionObject as pred}
    <ProgressLinear style="color: white; margin-bottom: 10px;" height="16px" value={pred.score * 100}>{pred.label}: {pred.score * 100}%</ProgressLinear>
{/each}

{#if winnerWinnerChickenDinner === 'Durchfahrt'}
  <p>The winning class is Durchfahrt with a high confidence!</p>
{:else if winnerWinnerChickenDinner === 'Ziellandung'}
  <p>The winning class is Ziellandung, but be careful, the confidence is not very high!</p>
{:else if winnerWinnerChickenDinner === 'Pfeiler'}
  <p>The winning class is Pfeiler, but the confidence is very low. You might want to double-check this!</p>
{:else if winnerWinnerChickenDinner === 'Abfahrtsstange'}
  <p>The winning class is Abfahrtsstange, but the confidence is extremely low. It's a good idea to verify this result!</p>
{:else}
  <p>The winning class is unknown. Please check the value of winnerWinnerChickenDinner!</p>
{/if}

{/if}
<img id="file_upload" style="max-height: 250px;" bind:this={img} alt="" />
