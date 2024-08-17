# Workflow: The goal of this program is to listen to phone chains on speakerphone and respond to them as neccessary
# to help get the doctor's question answered by a human. 
#
# Audio from phone call on speaker -> Whisper running locally, transcribing and submitting text to -> LLM, which has
# a prompt giving it the doctor's goal, the relevant information a doctor has (such as insurance codes, ID's, and 
# other relevant numbers that might be requested.) -> Text to speech library such as elevenlabs or competitor, and 
# also a DTMF phone number synthesizer to enter phone number options on number trees.
# 
