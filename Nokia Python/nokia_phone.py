menu_display = """
		Welcome to your Nokia Phone menu display
		List of Menu functions
		1 -> Phonebook
		2 -> Messages
		3 -> Chat
		4 -> Call Register
		5 -> Tones
		6 -> Settings
		7 -> Call divert
		8 -> Games
		9 -> Calculator
		10 -> Remainders
		11 -> Clock
		12 -> Profiles
		13 -> Sim settings

"""
print(menu_display)
menu_choice = int (input("Choose from the above menu: "))
match menu_choice: 
	case 1 : 		
		phonebook = """
			Phonebook
			1 -> Search
			2 -> Service Nos.
			3 -> Add name
			4 -> Erase
			5 -> Edit
			6 -> Assign Tone
			7 -> Send b'card
			8 -> Options
			9 -> Speed dials
			10 -> Voice tag
"""
		print(phonebook)
		phonebook_menu = int(input("Choose from the above phonebook dropdown menu: "))
		match phonebook_menu:
			case 1 : print("Search") 
			case 2 : print("Service Nos.") 
			case 3 : print("Add name")
			case 4 : print("Erase")
			case 5 : print("Edit")
			case 6 : print("Assign Tone")
			case 7 : print("Send b'card")
			case 8 : 
				options = """
				 Options
				1 -> Type of View
				2 -> Memory Status

"""
				print(options)
				options_menu = int(input("Choose from the above Options dropdown menu: "))
				match options_menu:
					case 1 : print("Type of View") 
					case 2 : print("Memory Status") 

			case 9 : print("Speed dials")
			case 10 : print("Voice tag")



	case 2 : 
		messages = """
			Messages
			1 -> Write messages
			2 -> Inbox
			3 -> Outbox
			4 -> Picture Messages
			5 -> Templates
			6 -> Smileys
			7 -> Message settings
			8 -> Info service
			9 -> Voice mailbox number
			10 -> Service command editor

"""
		print(messages)
		messages_menu = int(input("Choose from the above Messages dropdown menu: "))
		match messages_menu:
			case 1 : print("Write messages") 
			case 2 : print("Inbox") 
			case 3 : print("Outbox")
			case 4 : print("Picture Messages")
			case 5 : print("Templates")
			case 6 : print("Smileys")
			case 7 :
				messageSetting = """
				Messages Setting
				1 -> Set 1
				2 -> common
""";
				print(messageSetting)
				message_setting_menu = int(input("Choose from the above Message settings dropdown menu: "))
				match message_setting_menu:
					case 1 :
						set_1 = """
						Set 1
						1 -> Message center number
						2 -> Messages sent as
						3 -> Message validity
	
"""
						print(set_1) 
						set_1_menu = int(input("Choose from the above Set 1 dropdown menu: "))
						match set_1_menu:
							case 1 : print("Message center number")
							case 2 : print("Messages sent as")
							case 3 : print(" Message validity")

					case 2 : 
						common = """
						Common
						1 -> Delivery report
						2 -> Reply via same centre
						3 -> Character support

	
"""
						print(common) 
						common_menu = int(input("Choose from the above Common dropdown menu: "))
						match common_menu:
							case 1 : print(" Delivery report")
							case 2 : print("Reply via same centre")
							case 3 : print("Character support")



			case 8 : print("Info service")
			case 9 : print("Voice mailbox number")
			case 10 : print("Service command editor")


			
	case 3 : print("Chat")
	case 4 : 
		call_register = """
		Call Register
		1 -> Missed calls
		2 -> Received calls
		3 -> Dialed numbers
		4 -> Erase recent call lists
		5 -> Show call duration
		6 -> Show call costs
		7 -> Call cost settings
		8 -> Prepaid credit
		
			""";
		print(call_register) 
		call_registe_menu = int(input("Choose from the above Call Register  dropdown menu: "))
		match call_registe_menu:
			case 1 : print("Missed calls") 
			case 2 : print("Received calls") 
			case 3 : print("Dialed numbers")
			case 4 : print("Erase recent call lists")
			case 5 :
				show_call_duration = """
				Show call duration
				1 -> Last call duration
				2 -> All call's duration
				3 -> Recieved call's duration
				4 -> Dialed call duration
				5 -> Clear timer
"""
				print(show_call_duration)
				show_call_duration_menu = int(input("Choose from the above Show call duration drop down menu: "));
				match show_call_duration_menu:
					case 1 : print("Last call duration") 
					case 2 : print("All call's duration") 
					case 3 : print("Recieved call's duration")
					case 4 : print("Dialed call duration")
					case 5 : print("Clear timer")


			case 6 : 
				show_call_costs = """
				Show call costs
				1 -> Last call cost
				2 -> All call's cost											3 -> Clear counters
"""
				print(show_call_costs)
				show_call_costs_menu = int(input("Choose from the above Show call Costs dropdown menu: "))
				match show_call_costs_menu:
					case 1 : print("Last call costs") 
					case 2 : print("All call's cost") 
					case 3 : print(" Clear counters")

				
			case 7 :
				call_cost_settings = """
				Call cost settings
				1 -> call cost limit
				2 -> Show costs in					
"""
				print(call_cost_settings);
				call_cost_settings = int(input("Choose from the above Call cost settings dropdown menu: "));
				match call_cost_settings:
					case 1 : print(" Call costs limit") 
					case 2 : print("Show costs in") 

			case 8 : print("Prepaid credit")




	case 5 :
		tones = """
		Tones
		1 -> Ringing tone
		2 -> Ringing volume
		3 -> Incoming call alert
		4 -> Composer
		5 -> Message alert tones
		6 -> Keypad tones
		7 -> Warning and game tones
		8 -> Vibrating alert
		9 -> Screen saver
"""
		print(tones)
		tones_menu = int (input("Choose from the above Tones dropdown menu: "))
		match tones_menu:
				case 1 : print("Ringing tone") 
				case 2 : print("Ringing volume") 
				case 3 : print("Incoming call alert")
				case 4 : print("Composer")
				case 5 : print("Message alert tones")
				case 6 : print("Keypad tones") 
				case 7 : print("Warning and game tones")
				case 8 : print("Vibrating alert")
				case 9 : print("Screen saver")



	case 6 : 
		settings = """
			Settings
			1 -> Call Settings
			2 -> Phone settings
			3 -> Security settings
			4 -> Restore Factory Settings
			
"""
		print(settings)
		settings_menu = int(input("Choose from the above Settings dropdown menu: "))
		match settings_menu:
				case 1 : 
					call_setting = """
					Call Setting
					1 -> Automatic redial
					2 -> Speed dialing
					3 -> Call waiting options
					4 -> Own number sending
					5 -> Phone line in use
					6 -> Automatic answer
"""

					print(call_setting );
					call_setting_menu = int(input("Choose from the above Call settings dropdown menu: "))
					match call_setting_menu:
						case 1 : print("Automatic redial")  
						case 2 : print("Speed dialing") 
						case 3 : print("Call waiting options")
						case 4 : print("Own number sending")
						case 5 : print("Phone line in use") 
						case 6 : print("Automatic answer") 
				case 2 : 
					phone_setting = """
					Phone Setting
					1 -> Language
					2 -> Cell info display
					3 -> Welcome note
					4 -> Network selection
					5 -> Lights
					6 -> Confirm SIM service actions
"""


					print(phone_setting );
					phone_setting_menu = int(input("Choose from the above Phone settings dropdown menu: "))
					match phone_setting_menu:
						case 1 : print("Language")  
						case 2 : print("Cell info display") 
						case 3 : print(" Welcome note")
						case 4 : print("Network selection")
						case 5 : print("Lights") 
						case 6 : print("Confirm SIM service actions") 

				case 3 : 
					security_setting = """
					Security Setting
					1 -> Pin code request
					2 -> Call barring service
					3 -> Fixed dialing
					4 -> Closed user group
					5 -> Phone security
					6 -> Change access codes
"""



					print(security_setting);
					security_setting_menu = int(input("Choose from the above Security settings dropdown menu: "))
					match security_setting_menu:
						case 1 : print("Pin code request")  
						case 2 : print("Call barring service") 
						case 3 : print("Fixed dialing")
						case 4 : print("Closed user group")
						case 5 : print("Phone security") 
						case 6 : print("Change access codes") 
				case 4: print("Restore Factory Settings")





	case 7 : print("Call divert")
	case 8 : print("Games")
	case 9 : print("Calculator")
	case 10 : print("Remainders")
	case 11 : 
		clock = """
		Clock  
		1 -> Alarm clock
		2 -> Clock settings
		3 -> Date setting
		4 -> Stopwatch
		5 -> Countdown timer
		6 -> Auto update of date and tim
"""
		print(clock)
		clock_menu = int (input("Choose from the above Clock dropdown menu: "))
		match clock_menu:
				case 1 : print("Alarm clock") 
				case 2 : print("Clock settings") 
				case 3 : print("Date setting")
				case 4 : print("Stopwatch")
				case 5 : print("Countdown timer")
				case 6 : print("Auto update of date and time") 
		

	case 12 : print("Profiles")
	case 13 : print("Sim settings")
