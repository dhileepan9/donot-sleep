import script.display_on_notepad
import script.operate_file

filename = script.operate_file.create_filename()
count = 0
while count >= 0:
    count += 1
    script.operate_file.write_file(filename)
    script.display_on_notepad.notepad_runner(filename)
