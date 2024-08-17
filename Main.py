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
