// Pages
import Appartment from "./pages/Appartment.svelte";
import DrawClassification from "./pages/Draw.svelte";
import CatsClassification from "./pages/Cats.svelte";

import WebcamExample from "./pages/Webcam.svelte";

export default {
    // Home
    '/': Appartment,
    '/appartment': Appartment,

    // mnist draw example
    '/draw': DrawClassification,

    //cats (leopard, tiger, lion, cheeta)
    '/cats': CatsClassification,

    '/webcam': WebcamExample,

}