import speech_recognition as speech_recog
import text_to_speech
import speech_to_text
from playsound import playsound


#Returns None if can not determine the command type
def get_command_type (text):
    command = None
    if "see" in text or "front" in text or "seeing" in text:
        command = "Object Detection"
    elif "translation" in text or "translate" in text or "language" in text:
        command = "Translation"
    return command

#Loop to try to get the command from the user, breaks only if it gets its type
def take_command ():
    response = None
    first_time = True

    while True:

        if first_time:
            text_to_speech.play_text("Sightful is here for you, how can I help? I am listening")
            first_time = False

        response = speech_to_text.recognize_speech_from_microphone()

        #Speech recognition done successfully
        if (response["error"] is None):
            command = get_command_type(response["transcription"])
            if command is not None:
                text_to_speech.play_text("You asked for: " + command)
                return command
            else:
                text_to_speech.play_text("I did not get what you say, can you please repeat it? I am Listening.")
        
        elif(response["error"] == "API unavailable"):
            playsound('internet_error.mp3')
            break
        
        elif(response["error"] == "Unable to recognize speech"):
            text_to_speech.play_text("I did not get what you say, can you please repeat it? I am Listening.")


if __name__ == "__main__":
    print(take_command())
