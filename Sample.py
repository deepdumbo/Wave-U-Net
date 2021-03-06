import Metadata

class Sample(object):
    '''
    Represents a particular audio track - maintains metadata about the audio file for faster audio handling during training
    '''
    def __init__(self, path, sample_rate, channels, duration):
        self.path = path
        self.sample_rate = sample_rate
        self.channels = channels
        self.duration = duration


    @classmethod
    def from_path(cls, path):
        '''
        Create new sample object from audio file path by retrieving metadata.
        :param path: 
        :return: 
        '''

        sr, channels, duration = Metadata.get_audio_metadata(path)
        return cls(path, sr, channels, duration)

    @classmethod
    def from_array(cls, path, audio, sr):
        '''
        Create new sample object from a numpy audio array
        :param path:
        :return:
        '''

        channels = audio.shape[1]
        duration = float(audio.shape[0]) / float(sr)
        return cls(path, sr, channels, duration)