import speech_recognition as speech_recog

def recognize_speech_from_file (file_path, audio_offset = None, audio_duration = None):
    audio_file = speech_recog.AudioFile(file_path)
    recog = speech_recog.Recognizer()
    with audio_file as source:

        audio = recog.record(source, offset=audio_offset, duration=audio_duration)

        response = {
            "success": True,
            "error": None,
            "transcription": None
        }

        # Try recognizing the speech in the file.
        # If a RequestError or UnknownValueError exception is caught,
        # update the response object accordingly.
        try:
            response["transcription"] = recog.recognize_google(audio)
        except speech_recog.RequestError:
            # API was unreachable or unresponsive
            response["success"] = False
            response["error"] = "API unavailable"
        except speech_recog.UnknownValueError:
            # speech was unintelligible
            response["success"] = False
            response["error"] = "Unable to recognize speech"
        return response
    

def recognize_speech_from_microphone (time_limit = None):
    microphone  = speech_recog.Microphone()
    recog = speech_recog.Recognizer()
    with microphone  as source:
        print()
        print("Start Speaking")
        print()
        recog.adjust_for_ambient_noise(source)
        audio = recog.listen(source, phrase_time_limit=time_limit)

    print("Converting Speech to Text...\n")
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # Try recognizing the speech in the recording.
    # If a RequestError or UnknownValueError exception is caught,
    # update the response object accordingly.
        
    try:
        response["transcription"] = recog.recognize_google(audio)
    except speech_recog.RequestError:
        # API was unreachable or unresponsive
        response["success"] = False
        response["error"] = "API unavailable"
        print(speech_recog.RequestError)
    except speech_recog.UnknownValueError:
        # speech was unintelligible
        response["success"] = False
        response["error"] = "Unable to recognize speech"
    return response
