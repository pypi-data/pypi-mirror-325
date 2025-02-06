import sys
import asyncio
from Y2F_PACKAGE import Graphical_User_Interface, Youtube_Content_Operations


####################################
# YOUTUBE VIDEO DOWNLOAD INTERFACE #
####################################
async def Youtube_Download():
    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("link request menu")
    youtube_link = await gui.Graphical_User_Interface_Selector()

    if youtube_link.lower() == "_back":
        await main_entry_point()

    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("path selection menu")
    selected_path = await gui.Graphical_User_Interface_Selector()

    if selected_path.lower() == "_back":
        await main_entry_point()

    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("video downloading warning")
    await gui.Graphical_User_Interface_Selector()

    file_download = Youtube_Content_Operations.Operations("youtube video download", youtube_link, selected_path)
    file_download_result = await file_download.Operation_Selection()

    message = file_download_result
    await Message_Displayer(message)


##########################################
# YOUTUBE MP3 VIDEO CONVERSION INTERFACE #
##########################################
async def Youtube_Conversion():
    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("link request menu")
    youtube_link = await gui.Graphical_User_Interface_Selector()

    if youtube_link.lower() == "_back":
        await main_entry_point()

    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("path selection menu")
    selected_path = await gui.Graphical_User_Interface_Selector()

    if selected_path.lower() == "_back":
        await main_entry_point()

    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("video downloading warning")
    await gui.Graphical_User_Interface_Selector()

    file_download = Youtube_Content_Operations.Operations("youtube video conversion", youtube_link, selected_path)
    file_download_result = await file_download.Operation_Selection()

    message = file_download_result
    await Message_Displayer(message)


########################################
# YOUTUBE OPERATION FEEDBACK INTERFACE #
########################################
async def Message_Displayer(gui_message):
    try:
        gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages(gui_message)
        await gui.Graphical_User_Interface_Selector()

        gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("clear screen")
        await gui.Graphical_User_Interface_Selector()

        await main_entry_point()
    except KeyboardInterrupt:
        sys.exit(0)


##############################
# MAIN ENTRY POINT INTERFACE #
##############################
async def main_entry_point():
    gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("main menu")
    selected_input = (await gui.Graphical_User_Interface_Selector()).lower()

    if selected_input == "d":
        await Youtube_Download()
    elif selected_input == "c":
        await Youtube_Conversion()
    elif selected_input == "e":
        gui = Graphical_User_Interface.Graphical_User_Interfaces_For_Menus_And_Messages("clear screen")
        await gui.Graphical_User_Interface_Selector()
        sys.exit(0)
    else:
        await main_entry_point()


def main():
    asyncio.run(main_entry_point())


if __name__ == "__main__":
    main()
