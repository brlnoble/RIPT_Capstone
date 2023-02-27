import PySimpleGUI as sg

sg.theme('DefaultNoMoreNagging')
sg.theme_text_element_background_color('#EEE')
sg.theme_text_color('#333')
sg.theme_background_color('#EEE')

startLayout = [
	[sg.Text('Hit start to begin the inference'),],
	[sg.Button("Start",key="start_btn",enable_events=True)],
	[sg.Button("Exit",key="exit_btn",enable_events=True,button_color='Red')],
]

displayLayout = [
	[sg.Text('This is the results of the inference'),],
	[sg.Image(filename='',key='image')],
	[sg.Button("Exit",key="exit_btn",enable_events=True,button_color='Red')],
]


def GetStartWindow():
	return sg.Window("Startup",startLayout,keep_on_top=True)

def GetDisplayWindow():
	return sg.Window("Stream Test",displayLayout,keep_on_top=True)
