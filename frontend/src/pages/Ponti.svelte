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
  <p>Das Ziel ist es, ohne eine Berührung durch die mit einem Schweizerkreuz gekennzeichnete Durchfahrt zu gelangen, dies ergibt die Höchstpunktzahl von 10 Punkten. Die Durchfahrt besteht aus 6 Rohren (Brückenpfeiler-Markierungen) die an einem Seil herunterhängen. Die Distanz zwischen den Rohren beträgt 2,5 m. Werden die Rohre mit dem Boot oder Ruder berührt, ergibt dies einen Punktabzug je Berührung. Wird ein Rohr mit dem Joch (Spitze des Schiffes) berührt, zählt die nächst tiefere Ziel Note markiert mit „8“ oder „6“. Wird eine Hilfsmarkierung mit den Händen berührt oder fällt diese gar ins Schiff, wird dies mit Punkteabzügen geahndet. </p>
{:else if winnerWinnerChickenDinner === 'Ziellandung'}
  <p>Das Schiff ist so zu steuern, dass es mit dem Vorderteil (Bug) flussaufwärts gerichtet, ohne Aufprallen am Ufer anlegt. Die Landung hat in Parallelstellung zu erfolgen. Massgebend für die Ziellandung ist immer die landseitige vordere Joch Ecke des Schiffes. Das Schweizerkreuz symbolisiert zugleich die Höchstnote 10. Nachdem der 1. Stachel im Wasser ist, darf sich das Schiff im Maximum ½ Punkt zu Gunsten der Ziel Note verschieben. </p>
{:else if winnerWinnerChickenDinner === 'Pfeiler'}
  <p>Die Durchfahrt besteht aus 6 Rohren (Brückenpfeiler-Markierungen) die an einem Seil herunterhängen. Die Distanz zwischen den Rohren beträgt 2,5 m. Werden die Rohre mit dem Boot oder Ruder berührt, ergibt dies einen Punktabzug je Berührung. Wird ein Rohr mit dem Joch (Spitze des Schiffes) berührt, zählt die nächst tiefere Ziel Note markiert mit „8“ oder „6“. Wird eine Hilfsmarkierung mit den Händen berührt oder fällt diese gar ins Schiff, wird dies mit Punkteabzügen geahndet.</p>
{:else if winnerWinnerChickenDinner === 'Abfahrtsstange'}
  <p>Die Stange ist in verschiedene Felder aufgeteilt, zu sehen an den farblich unterschiedlichen Markierungen. Im äußersten Feld ist ein sogenannter Lappen montiert. Wird dieser mit der Spitze des Schiffes berührt, erhält das Fahrerpaar die Höchstpunktzahl von 10 Punkten. Wird der Lappen nicht berührt, wird vom Land aus mit Hilfe einer fahrbaren Skalierung die Distanz zur Stange im äußersten Feld gemessen. Je nach gemessener Distanz werden die Punkte verteilt. Wird die Stange jedoch berührt, erhält das Fahrerpaar Punktabzüge. Im ersten Feld vom Land aus sind dies 4 Punkte, im zweiten sind es 3 Punkte, im dritten sind es 2 Punkte und im äußersten Feld, wo auch der Lappen hängt, ist es 1 Punkt.

  </p>
{:else}
  <p>The winning class is unknown. Please check the provided image!</p>
{/if}

{/if}
<img id="file_upload" style="max-height: 250px;" bind:this={img} alt="" />
