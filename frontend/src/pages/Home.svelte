<div class="pb-4 align-center">
      <h1>Willkommen auf dem neuen PCMT</h1>
</div>
<div>
    <h4>
        Motivation
    </h4>
<div>
    <h6>
        End users (text)
    </h6>
    <p>
        This applications is designed for visitors that come and visit our competitions. Momentatrly they can only use the application to get some insights in the objects the competitors have to overcome.
    </p>
</div>
<div>
    <h6>
        Goal of end users (text)
    </h6>
    <p>
       As an enduser I want to understand what each object is and what it is used for.
</p>
</div>
<div>
    <h6>
        Obstacle to be solved (text)
    </h6>
    <p>
      Since pontonier is a pretty unknown but cool looking sport we often get spectators at competitions aswell as trainings. They often ask what the objects are and what they are used for. We want to give them the opportunity to find out themselves and in a modern fashion.
</p>
</div>
</div>
<div>
    <h4>Data Collection and Augmentation</h4>
    <div>
        <h6>Images Collected</h6>
        <p>
            The Images are stored on a seperate Harddrive. To be able to hand them in they have been deployed to a Google Drive.
        </p>
    </div>
    <div>
        <h6>Description of splitting images into classes/labelling images (text)</h6>
        <p>
            The images have been split into classes by hand. The classes are the objects that are used in the sport. The images have been gathered from Friends, Family and other Sections as well as the SPSV which was kind enough to give them to me.
            At the moment there are 4 classes in the Classification. 
        </p>
            <ul>
                <li>Abfahrtsstange</li>
                <li>Pfeiler</li>
                <li>Ziellandung</li>
                <li>Durchfahrt</li>
            </ul>
        <p>Officially the Pontonier sport has some more Objects but they are rarely used and therefore even harder to get images from.</p>

    </div>
    <div>
        <h6>Data Augmentation description (text)</h6>
        <p>
            To handle my small dataset I used data augmentation. I used the ImageDataGenerator from Keras to augment my data. I used the following augmentations:

        </p>

    </div>
</div>

<div>
    <h4>Results of User Validation</h4>

    <p>Sadly I wasn't able to test it at an actual competition but I was able to use our trainingobjects which did the job. I also handed the project to Gregory Hill, Calvin Scheidegger and Michael Neukom to have a go at it.
        In summary they were thrilled about the application and finally understood what they were taking pictures from (especially Greg)
    </p>
</div>

<diV>
    <h3>This was pretty dope right?</h3>
    <a class="btn btn-primary" href="/#/ponti" >GO CHECK IT OUT</a>
    
</diV>