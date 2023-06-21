// Pages
import Home from "./pages/Home.svelte";

import PontiClassification from "./pages/Ponti.svelte";

import WebcamExample from "./pages/Webcam.svelte";

export default {
    // Home
    '/': Home,
    //cats (leopard, tiger, lion, cheeta)
    '/ponti': PontiClassification,

    '/webcam': WebcamExample,

}