import numpy as np
import wave
import subprocess
import matplotlib.pyplot as plt
import speech_recognition as sr

# from .audio import AudioData, get_flac_converter
from speech_recognition import AudioData


class SpeechToText:
    """ """

    def __init__(self):
        self.text = ""
        self.audio_frames = []
        self.word_frame = 0
        self.stop_log = False

        self.english_words = []
        self.dutch_words = []
        self.silance_time = 1
        self.silance_threshold = 1000
        self.silance_threshold2 = 10

        self.sample_rate = 16000

        self.mode_continues = False
        self.new_words = False
        self.processing = False
        self.silence_counter = 0
        self.to_proses_frames = []

        self.do_speach = True
        self.logging = False

        # subprocess.run("rm -rf output/*", shell=True)

        # self.loop()

    def logger(self, string):
        if self.logging:
            print(string)

    def loop(self):
        if self.processing:
            self.logger("start prosesor")
            self.proses_audio(self.to_proses_frames.pop())

    def get_text(self):
        return self.text

    def listen(self, data):
        frame_single = data["data"]["body.head"]
        if frame_single is None:
            pass
        else:
            audio_np = np.frombuffer(frame_single, dtype=np.int16)
            # print(audio_np)
            self.logger(f"audio frame {audio_np[0]}")
            self.audio_frames.append(audio_np)

    def listen_split(self, data):
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
        if self.do_speach:
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
                    if abs(packet) < self.silance_threshold2:
                        self.silence_counter += 1
                    else:
                        # print("reset silance")
                        # pass
                        self.silence_counter -= 1
                        if self.silence_counter < 0:
                            self.silence_counter = 0
                        # self.silence_counter = self.silence_counter/1.1
                        # self.silence_counter =0

                # try:
                #     if abs(audio_np[0]) > self.silance_threshold2:
                #         self.silence_counter +=1
                #     else:
                #         self.silence_counter -=1
                # except:
                #     pass

                # print(f"silance counter :{self.silence_counter}")

                min_silence_samples = int(self.sample_rate * self.silance_time)
                if (
                    self.silence_counter > min_silence_samples
                    and self.processing == False
                ):
                    self.silence_counter = 0
                    self.logger("got silance")
                    self.processing = True
                    self.to_proses_frames.append(self.audio_frames)
                    # self.proses_audio(self.to_proses_frames)
                    self.audio_frames = []
                    self.silence_counter = 0
        else:
            self.audio_frames = []
            pass

    def split_audio(self, audio_data):
        silence_threshold = 100
        # min_silence_duration = self.silance_time
        sample_rate = 16000
        min_silence_samples = int(sample_rate * self.silance_time)

        silent_regions = np.where(np.abs(audio_data) < silence_threshold)[0]

        if len(silent_regions) == 0:
            return [audio_data]

        # Find silence segment start and end indices
        split_points = []
        prev_silent_sample = silent_regions[0]
        for i in range(1, len(silent_regions)):
            if silent_regions[i] - prev_silent_sample > 1:
                if (
                    silent_regions[i] - split_points[-1] > min_silence_samples
                    if split_points
                    else True
                ):
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

    def proses_audio(self, input_audio):
        self.logger("proses audio")
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
        self.logger("give me words")
        self.new_words = False
        return self.english_words
        return [self.dutch_words, self.english_words]

    def plot_audio_frames(self, data):
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
        peak = np.max(np.abs(audio_data))
        if peak == 0:
            return audio_data

        normalization_factor = target_peak / peak

        normalized_audio = (audio_data * normalization_factor).astype(np.int16)
        return normalized_audio

    def save_audio(self, audio_data):
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
