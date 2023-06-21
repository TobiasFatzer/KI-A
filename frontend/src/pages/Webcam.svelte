<script>
    import { onMount } from "svelte";
    import axios from "axios";

    let huggingFaceLoading = false;

    let prediction = "";

    let VIDEO;
    let ENABLE_CAM_BUTTON;
    let videoPlaying;
    let hasPictuteBeenTaken = false;
    let huggingFaceErrorMessage = '';

    let canvas;
    let context;

    let width = 640;
    let height = 480;

    function hasGetUserMedia() {
        return !!(
            navigator.mediaDevices && navigator.mediaDevices.getUserMedia
        );
    }

    function enableCam() {
        if (hasGetUserMedia()) {
            // getUsermedia parameters.
            const constraints = {
                video: true,
                width: width,
                height: height,
            };

            // Activate the webcam stream.
            navigator.mediaDevices
                .getUserMedia(constraints)
                .then(function (stream) {
                    VIDEO.srcObject = stream;
                    VIDEO.addEventListener("loadeddata", function () {
                        videoPlaying = true;
                        ENABLE_CAM_BUTTON.classList.add("removed");
                    });
                });
        } else {
            console.warn("getUserMedia() is not supported by your browser");
        }
    }

    function snap() {
        context.drawImage(VIDEO, 0, 0, canvas.width, canvas.height);
        hasPictuteBeenTaken = true;
    }

    function convertCanvasToData(){
        canvas.toBlob((blob) => {
              predict(blob);
          }, "image/jpeg");
    }
    
    function predict(data) {
      let url =
          "https://api-inference.huggingface.co/models/kuhs/cats_classficiation";
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

    onMount(() => {
        context = canvas.getContext("2d");
    });
</script>

{#if huggingFaceLoading}
  <h3>{huggingFaceErrorMessage}</h3>
{/if}
<div class="container">
    {#if prediction !== ""}
    <div class="row">
        <div class="col col-lg-2">predictions:</div>
        <div class="col col-lg-10">{prediction}</div>
    </div>
    {/if}
    <div class="row">
        <div class="col col-lg-6">
            <video bind:this={VIDEO} id="webcam" height="{height}" width="{width}" autoplay muted />

            <button bind:this={ENABLE_CAM_BUTTON} on:click={enableCam}
                >Enable Webcam</button
            >
            <button on:click={snap}>Take Picture</button>
        </div>

        <div class="col col-lg-6">
            <canvas bind:this={canvas} {width} {height} />
            {#if hasPictuteBeenTaken}
                <button on:click={convertCanvasToData}>Predict</button>
            {/if}
        </div>
    </div>
</div>

<style>
    canvas {
        padding-left: 5px;
    }
</style>
