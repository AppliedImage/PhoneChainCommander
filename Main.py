# Workflow: The goal of this program is to listen to phone chains on speakerphone and respond to them as neccessary
# to help get the doctor's question answered by a human. 
#
# Audio from phone call on speaker -> Whisper running locally, transcribing and submitting text to -> LLM, which has
# a prompt giving it the doctor's goal, the relevant information a doctor has (such as insurance codes, ID's, and 
# other relevant numbers that might be requested.) -> Text to speech library such as elevenlabs or competitor, and 
# also a DTMF phone number synthesizer to enter phone number options on number trees. -> Updates from this system 
# presented to the user, along with a transcription to help them orient themselves as to what is currently happening.
# A tone beeps whenever the user needs to actively engage with the phone calls. 
#
# The use case looks like the doctor writing their goal, inputting the information they have, and then calling the 
# first number they need to speak with. They put their phone on speaker, and the program begins transcribing and sending
# the call information for the LLM to decide what to do next to get the doctor's goal met, using DTMF tones and synthesized
# speech as necessary.
#
# Prompt for LLM:

# "Your task is to assist Dr. [Doctor's Name] in navigating a phone call to achieve the following goal:
# [Doctor's Goal]. The patient in question is [Patient's Name], with the following relevant details: [Patient's Medical History], [Current Medications], and [Insurance Information, including Member ID]. Dr. [Doctor's Name]'s identification numbers are as follows: NPI - [NPI Number], Date of Birth - [DOB], Practice Tax ID - [Tax ID]. Use this information to answer questions, navigate phone trees, and interact with representatives, ensuring the doctor’s goal is met."
#
#_______________________________________________________________________________________________________________________

# Import necessary libraries
# - Import libraries for audio processing, speech recognition (Whisper), language model interaction (ChatGPT API),
#   text-to-speech conversion (OpenVoice V2), DTMF tone generation, and GUI for user interface.

# Define global variables
# - Set up global variables for storing the doctor's input, including patient information, goal, and doctor’s details.

# Initialize the audio input stream
# - Set up the microphone or audio input from the phone's speaker to capture the ongoing call.

# Implement Whisper transcription
# - Continuously transcribe the incoming audio from the call using Whisper.
# - Store the transcriptions and pass them to the language model for further processing.

# LLM prompt construction
# - Construct the LLM prompt dynamically using the global variables (doctor’s input).
# - This prompt will guide the LLM's decision-making during the call.

# LLM processing loop
# - Send each transcription to the LLM along with the constructed prompt.
# - Analyze the LLM's response to determine the next action (e.g., respond with TTS, generate DTMF tones, or pause for user input).

# Error handling mechanism
# - Implement error detection to monitor the transcription accuracy and the LLM's confidence in its decisions.
# - If errors are detected, trigger the fallback mechanisms or request manual input from the doctor.

# Contextual memory management
# - Store and update contextual information throughout the call session to maintain continuity and relevance in the LLM’s responses.

# TTS and DTMF generation
# - Convert LLM-generated text responses into speech using OpenVoice V2.
# - Generate DTMF tones when navigating phone trees or entering numeric information.

# User interface updates
# - Update the GUI with real-time transcriptions, LLM responses, and prompts for manual input when necessary.
# - Provide visual and auditory cues to alert the doctor when their attention is needed.

# Manual override feature
# - Allow the doctor to manually intervene and input commands directly into the system if needed.

# Customization options
# - Implement functionality to allow the doctor to customize the LLM's prompt before starting the call, including specific instructions and preferences.

# End of call cleanup
# - Safely terminate the audio stream, save session data, and clear any sensitive information from memory.

# Main program loop
# - Continuously run the above processes in a loop until the call ends or the doctor chooses to stop the system.

# Execution entry point
# - Define the main function that initializes and runs the entire program, handling any exceptions and ensuring smooth operation.
