# KI-A

Problem Statement and Motivation:

End users: People who are interested in evaluating boat positions relative to certain objects.
Goal of end users: Accurately assign a score/value to a "Ziellandung" depending on where a boat lands.
Obstacle to be solved: Automating the process of scoring a "Ziellandung" based on boat position, removing the need for manual assessment.

Data Collection and Augmentation:

Collect images of each object (Ziellandung, Pfeiler, Durchfahrt, Abfahrtsstange). Also, gather images of boats in different landing positions relative to a "Ziellandung". Label these images accordingly.
Augment data: Apply image augmentation techniques to increase the size of your dataset and reduce overfitting.

Model Training:

Train a model to recognize the objects (Ziellandung, Pfeiler, Durchfahrt, Abfahrtsstange). This would be an object detection task.
Train a separate model (or an extension of the first model) to assign a value to a "Ziellandung" based on the boat's landing position. This could be a regression or classification task, depending on the nature of your scores/values.

Model Application and Deployment:

Develop an application that takes in an image, recognizes the objects using your object detection model, and then assigns a score to the "Ziellandung" based on the boat's landing position using your second model.
Deploy your application on a suitable platform. The application should allow users to upload an image and receive a score for the "Ziellandung".
