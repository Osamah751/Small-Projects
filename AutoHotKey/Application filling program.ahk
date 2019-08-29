;Turn off the app
;	LControl & Esc::ExitApp

;--------------------------------------
looping := false 
global DELAY := 500 ;ms
password = 
(
First_name	|Surname	|Email	|Phone_Number	|BU_ID	|BU_Email
)	

F10::
	looping := true

    Loop, Parse, password, |
	{

		Send, %a_loopfield%
		Sleep, DELAY
		;Send, {Tab}
		
		if (looping = false)
			break
	}
		Send, {Tab}
		Send, {Tab}
		Send, {Space}
		
		Send, {Tab}
		Send, {Tab}
	return



F9::
	if (looping = true)
		Send, Ty
			Sleep, 500
		Send, {Backspace}
		Send, {Backspace}
		looping := false
		
	return
	
;---------------------------------------
; select all and copy
	^z::
		Send ^{a}
		Send ^{c}