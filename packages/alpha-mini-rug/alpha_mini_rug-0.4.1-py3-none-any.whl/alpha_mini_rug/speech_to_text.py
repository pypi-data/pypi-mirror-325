import numpy as np
import wave
import subprocess
import matplotlib.pyplot as plt
import speech_recognition as sr

# from .audio import AudioData, get_flac_converter
from speech_recognition import AudioData


class SpeechToText:
    """
    Class for converting audio to text
    """

    def __init__(self):
        self.text = ""
        self.audio_frames = []
        self.word_frame = 0
        self.stop_log = False

        self.english_words = []
        self.dutch_words = []
        self.silence_time = 1
        self.silence_threshold = 1000
        self.silence_threshold2 = 10

        self.sample_rate = 16000

        self.mode_continues = False
        self.new_words = False
        self.processing = False
        self.silence_counter = 0
        self.to_process_frames = []

        self.do_speech_recognition = True
        self.logging = False

        # subprocess.run("rm -rf output/*", shell=True)

        # self.loop()

    def logger(self, string):
        """
        Logs a given string if logging is enabled.

        Args:
            string (str): The string to be logged.
        """
        if self.logging:
            print(string)

    def loop(self):
        """
        Continuously processes audio frames if processing is active.

        This method checks if the processing flag is set to True. If it is,
        it logs the start of the processor and processes the next audio frame
        from the to_process_frames list.

        Note:
            Ensure that the to_process_frames list is not empty before calling
            this method to avoid IndexError.

        Attributes:
            processing (bool): Flag indicating whether processing is active.
            logger (function): Function to log messages.
            process_audio (function): Function to process audio frames.
            to_process_frames (list): List of audio frames to be processed.
        """
        if self.processing:
            self.logger("start processor")
            self.process_audio(self.to_process_frames.pop())

    def get_text(self):
        """
        Retrieves the text.

        Returns:
            str: The text stored in the instance.
        """
        return self.text

    def listen(self, data):
        """
        Processes incoming audio data and appends it to the audio frames list.

        Args:
            data (dict): A dictionary containing audio data. The audio data is expected to be found
                         under the key "data" and subkey "body.head".

        Returns:
            None
        """
        frame_single = data["data"]["body.head"]
        if frame_single is None:
            pass
        else:
            audio_np = np.frombuffer(frame_single, dtype=np.int16)
            # print(audio_np)
            self.logger(f"audio frame {audio_np[0]}")
            self.audio_frames.append(audio_np)

    def listen_split(self, data):
        """
        Processes incoming audio data and appends it to the audio frames list.

        Args:
            data (dict): A dictionary containing audio data. The audio data is expected to be found
                         at data["data"]["body.head"].

        Returns:
            None

        Raises:
            None

        Notes:
            - If the audio data is None, the function does nothing.
            - If the audio data is not None, it converts the audio data from a buffer to a numpy array
              of int16 type and appends it to the audio_frames list.
            - Logs the first element of the audio frame if logging is enabled.
            - If an exception occurs during appending, it logs an error message.
        """
        self.mode_continues = False
        frame_single = data["data"]["body.head"]
        if frame_single is None:
            pass
        else:
            audio_np = np.frombuffer(frame_single, dtype=np.int16)
            # print(audio_np)
            try:
                if self.stop_log == False:
                    self.logger(f"audio frame {audio_np[0]}")
                self.audio_frames.append(audio_np)
                # if len(self.audio_frames) > 500:
                # self.audio_splitter()

            except:
                self.logger("can not append")

    def listen_continues(self, data):
        """
        Processes continuous audio data for speech recognition.
        This method listens to incoming audio data and processes it for speech recognition.
        It appends audio frames to a buffer and detects silence to determine when to process
        the buffered audio frames.
        Args:
            data (dict): A dictionary containing audio data. The audio data is expected to be
                         in the format data["data"]["body.head"].
        Attributes:
            do_speech_recognition (bool): A flag indicating whether speech recognition is enabled.
            mode_continues (bool): A flag indicating whether continuous mode is active.
            audio_frames (list): A list to store audio frames.
            stop_log (bool): A flag indicating whether logging is stopped.
            silence_counter (int): A counter to track the number of silent audio frames.
            silence_threshold2 (int): A threshold value to determine silence in audio frames.
            sample_rate (int): The sample rate of the audio data.
            silence_time (float): The duration of silence to detect in seconds.
            processing (bool): A flag indicating whether audio processing is ongoing.
            to_process_frames (list): A list to store frames to be processed.
        Raises:
            Exception: If there is an error appending audio frames to the buffer.
        """

        if self.do_speech_recognition:
            self.mode_continues = True
            frame_single = data["data"]["body.head"]
            # print(len(self.audio_frames))
            if frame_single is None:
                pass
            else:
                audio_np = np.frombuffer(frame_single, dtype=np.int16)
                # print(audio_np)
                try:
                    if self.stop_log == False:
                        # print(f"audio frame {audio_np[0]}")
                        pass
                    self.audio_frames.append(audio_np)

                except:
                    self.logger("can not append")

                for packet in audio_np:
                    # print(f"packet: {packet}")
                    if abs(packet) < self.silence_threshold2:
                        self.silence_counter += 1
                    else:
                        # print("reset silence")
                        # pass
                        self.silence_counter -= 1
                        if self.silence_counter < 0:
                            self.silence_counter = 0
                        # self.silence_counter = self.silence_counter/1.1
                        # self.silence_counter =0

                # try:
                #     if abs(audio_np[0]) > self.silence_threshold2:
                #         self.silence_counter +=1
                #     else:
                #         self.silence_counter -=1
                # except:
                #     pass

                # print(f"silence counter :{self.silence_counter}")

                min_silence_samples = int(self.sample_rate * self.silence_time)
                if self.silence_counter > min_silence_samples and self.processing == False:
                    self.silence_counter = 0
                    self.logger("got silence")
                    self.processing = True
                    self.to_process_frames.append(self.audio_frames)
                    # self.process_audio(self.to_process_frames)
                    self.audio_frames = []
                    self.silence_counter = 0
        else:
            self.audio_frames = []
            pass

    def split_audio(self, audio_data):
        """
        Splits the given audio data into chunks based on detected silence.

        Parameters:
        audio_data (numpy.ndarray): The audio data to be split.

        Returns:
        list: A list of numpy arrays, each representing a chunk of the original audio data.

        The method works by identifying regions of silence in the audio data and using these regions as split points.
        Silence is defined as audio samples with an absolute value below a certain threshold. The method also ensures
        that chunks shorter than a specified length are removed.

        The method logs the number of detected chunks, the length of each chunk, and the number of chunks left after
        removing short chunks.
        """
        silence_threshold = 100
        # min_silence_duration = self.silence_time
        sample_rate = 16000
        min_silence_samples = int(sample_rate * self.silence_time)

        silent_regions = np.where(np.abs(audio_data) < silence_threshold)[0]

        if len(silent_regions) == 0:
            return [audio_data]

        # Find silence segment start and end indices
        split_points = []
        prev_silent_sample = silent_regions[0]
        for i in range(1, len(silent_regions)):
            if silent_regions[i] - prev_silent_sample > 1:
                if silent_regions[i] - split_points[-1] > min_silence_samples if split_points else True:
                    split_points.append(prev_silent_sample)
            prev_silent_sample = silent_regions[i]

        # Split audio based on detected silence
        chunks = []
        start = 0
        for split in split_points:
            newstart = max(0, start - 500)
            newend = min(len(audio_data), split + 500)
            chunks.append(audio_data[newstart:newend])
            start = split
        chunks.append(audio_data[start:])  # Add the last chunk

        self.logger(f"detected chunks: {len(chunks)}")
        ammount_of_chunks = len(chunks)

        for chunk_number in range(ammount_of_chunks - 1):
            self.logger(f"chunk {chunk_number} length: {len(chunks[chunk_number])}")
            if len(chunks[chunk_number]) < 5000:
                chunks.pop(chunk_number)
                self.logger(f"chunk {chunk_number} removed")

        self.logger(f"chunks left over: {len(chunks)}")
        return chunks

    def process_audio(self, input_audio):
        """
        Processes the input audio data and performs speech-to-text conversion.

        Args:
            input_audio (list of numpy arrays): A list of numpy arrays containing audio data.

        Returns:
            None

        This method performs the following steps:
        1. Logs the start of audio processing.
        2. Concatenates all input audio data into a single numpy array.
        3. Normalizes the concatenated audio data.
        4. Depending on the mode (continuous or not), it either splits the audio into word packets or processes the entire audio.
        5. If in non-continuous mode, it saves and converts each word packet to text.
        6. If in continuous mode, it saves and converts the entire audio to text if its length exceeds a threshold.
        7. Logs the length of the audio and stops recognition if the audio is too short.
        8. Sets the processing flag to False when done.
        """
        self.logger("process audio")
        self.stop_log = True
        all_audio_data = np.concatenate(input_audio)
        normalized_audio = self.normalize_audio(all_audio_data)

        # self.save_audio(normalized_audio)
        # self.plot_audio_frames(normalized_audio)

        if not self.mode_continues:
            word_packets = self.split_audio(normalized_audio)

            self.logger(f"word packets: {len(word_packets)}")
            if len(word_packets) > 0 and len(word_packets) < 10:
                for word in word_packets:
                    self.save_audio(word)
                    self.speech_to_text(word)
        else:
            self.logger(f"audio lenth {len(normalized_audio)}")
            if len(normalized_audio) > 8000:
                self.save_audio(normalized_audio)
                self.speech_to_text(normalized_audio)
            else:
                self.logger("stopping recognision")

                # self.plot_audio_frames(word)
        self.processing = False

    def speech_to_text(self, data):
        """
        Converts speech from an audio file to text using Google's speech recognition API.

        Args:
            data: The input data for the speech to text conversion (not used in the current implementation).

        Returns:
            None

        Side Effects:
            - Logs the process of speech to text conversion.
            - Appends recognized Dutch text to self.dutch_words.
            - Appends recognized English text to self.english_words.
            - Sets self.new_words to True if new words are recognized.

        Raises:
            Exception: If the speech recognition fails, logs an error message.
        """
        languages = ["nl-NL", "en-US"]

        self.logger("speech to text")

        if not self.mode_continues:
            filename = f"output/output{self.word_frame-1}.wav"
        else:
            filename = "output/output.wav"

        recognizer = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio_data = recognizer.record(source)
            # todo use

        # audio_data= AudioData(source, self.sample_rate, 2)

        try:
            # todo make is a setting
            # text = recognizer.recognize_google(audio_data, language=languages[0])
            self.dutch_words.append("text")
            # text = recognizer.recognize_whisper_api(audio_data)
            # print(f"Recognized text: {text}")
            text = recognizer.recognize_google(audio_data, language=languages[1])
            self.english_words.append(text)
            self.logger(f"Recognized text: {text}")
            self.new_words = True
        except:
            self.logger("can not recognize")

    def give_me_words(self):
        """
        Retrieve the list of English words.
        This method logs the action, sets the `new_words` attribute to False,
        and returns the list of English words stored in the `english_words` attribute.
        Returns:
            list: A list of English words.
        """

        self.logger("give me words")
        self.new_words = False
        return self.english_words

    def plot_audio_frames(self, data):
        """
        Plots the audio frames from the given data and saves the plot as an image.
        Parameters:
        data (array-like): The audio data to be plotted.
        The function creates a plot of the audio frames with the x-axis representing the sample index and the y-axis representing the amplitude.
        The plot is saved as 'output/plot.png'. If an error occurs during plotting, an error message is logged.
        """

        try:
            plt.figure(figsize=(10, 4))
            plt.plot(data)
            plt.title("Audio Frames")
            plt.xlabel("Sample Index")
            plt.ylabel("Amplitude")
            plt.savefig(f"output/plot.png")
            plt.close()
        except:
            self.logger("can not plot")

    def normalize_audio(self, audio_data, target_peak=32767):
        """
        Normalize the audio data to a target peak value.
        Parameters:
        audio_data (numpy.ndarray): The input audio data array.
        target_peak (int, optional): The target peak value for normalization. Default is 32767.
        Returns:
        numpy.ndarray: The normalized audio data array.
        """

        peak = np.max(np.abs(audio_data))
        if peak == 0:
            return audio_data

        normalization_factor = target_peak / peak

        normalized_audio = (audio_data * normalization_factor).astype(np.int16)
        return normalized_audio

    def save_audio(self, audio_data):
        """
        Save the provided audio data to a WAV file.

        Parameters:
        audio_data (numpy.ndarray): The audio data to be saved.

        The audio is saved with a sample rate of 16000 Hz, 1 channel, and a sample width of 2 bytes.
        If `self.mode_continues` is False, the audio is saved to a file named "output/output{self.word_frame}.wav".
        Otherwise, it is saved to "output/output.wav".

        The method increments `self.word_frame` after successfully saving the file.

        Logs a message indicating the file being saved. If an error occurs during saving, logs an error message.
        """
        sample_rate = 16000
        channels = 1
        sampwidth = 2

        if not self.mode_continues:
            filename = f"output/output{self.word_frame}.wav"
        else:
            filename = "output/output.wav"

        try:
            self.logger(f"Saving audio file {self.word_frame}")
            with wave.open(filename, "wb") as wav_file:
                wav_file.setnchannels(channels)
                wav_file.setsampwidth(sampwidth)
                wav_file.setframerate(sample_rate)
                wav_file.writeframes(audio_data.tobytes())
                self.word_frame += 1
        except:
            self.logger("can not save file")
