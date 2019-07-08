;Turn off the app
	LControl & Esc::ExitApp

;--------------------------------------
; turn the code off

	RControl & LButton::Pause, Toggle

;---------------------------------------
; for mining stone
; holding (left click + shift)
	
	RControl & RButton::
		delay = 200000
		
		loop 8
		{
			
			Send {LButton down}
			sleep, delay
			Send {LButton up}
		
			loop 5
				Click, WheelDown
		}
			Send {LButton down}
			sleep, delay
			Send {LButton up}
		