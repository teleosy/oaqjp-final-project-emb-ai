"""
This module contains a Flask server that runs an emotion detector
"""
from flask import Flask, render_template, request

# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid input! Please try again."

    return (
        f"For the given statement, the system response is "
        f"anger': {response['anger']}, "
        f"disgust': {response['disgust']}, "
        f"fear': {response['fear']}, "
        f"joy': {response['joy']}, "
        f"sadness': {response['sadness']}, "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
