import os
import sys


#########################################
# CLASS THAT MANAGES YOUTUBE OPERATIONS #
#########################################
class Operations:
    chosen_operation = None
    chosen_path = None
    youtube_link = None

    def __init__(
            self,
            init_chosen_operation,
            init_youtube_link,
            init_chosen_path
    ):
        self.chosen_operation = init_chosen_operation
        self.chosen_path = init_chosen_path
        self.youtube_link = init_youtube_link

    #########################################################################
    # SELECTS THE YOUTUBE OPERATION ( MP4 TO MP3 DOWNLOAD OR MP4 DOWNLOAD ) #
    #########################################################################
    async def Operation_Selection(self) -> str:
        download_result = await self.__Youtube_Download()
        return download_result

    #######################################################################################
    # DOWNLOAD THE MP4 VIDEO OR AUDIO FILE BINARY DATA AND STORE IT IN THE OS FILE SYSTEM #
    #######################################################################################
    async def __Youtube_Download(self) -> str:
        try:
            from pytubefix import YouTube, exceptions
            youtube_object = YouTube(
                url=self.youtube_link, use_oauth=True,
                allow_oauth_cache=True,
                client="WEB",
            )

            if os.path.exists(self.chosen_path) is True:
                if self.chosen_operation == "youtube video conversion":
                    video_audio = youtube_object.streams.get_audio_only()

                    audio_path = video_audio.download(output_path=self.chosen_path)

                    os.rename(
                        audio_path,
                        audio_path
                        + ".mp3",
                    )

                    return audio_path

                else:
                    video = youtube_object.streams.get_highest_resolution(progressive=True)
                    path = video.download(output_path=self.chosen_path)
                    return path
            else:
                return "path not found"

        except Exception as e:
            if e == ModuleNotFoundError:
                return "module not found"
            elif e == "regex_search: could not find match for":
                return "wrong link"
            elif "is age restricted" in str(e):
                return "age restricted video"
            else:
                return "unknown error"
