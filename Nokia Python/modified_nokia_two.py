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
		0 -> Exit

"""
menu_display_going = True
while(menu_display_going):
	print(menu_display)
	menu_choice =  input("Choose from the above menu: ")
	match menu_choice: 
		case "1" : 		
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
				0 -> Previous menu
"""	
			phonebook_going = True
			while(phonebook_going):
				print(phonebook)
				phonebook_menu = input("Choose from the above phonebook dropdown menu: ")
				match phonebook_menu:
					case "1" : 
						search = True
						while(search):
							print("	Search...")
							print(" 	0 -> Previous menu")
							search_menu = input("Choose 0 to go back to previous menu: ")
						
  	
							match search_menu:
								case "1" : print("Invalid Input, Please go back to previous menu")
								case "0" : search = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "2" : 
						service_no  = True
						while(service_no):
							print("	Service Nos...")
							print(" 	0 -> Previous menu")
							service_no_menu = input("Choose 0 to go back to previous menu: ")
						
  	
							match service_no_menu:
								case "0" : service_no = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "3" : 
						add_name  = True
						while(add_name):
							print("	Add name...")
							print(" 	0 -> Previous menu")
							add_name_menu = input("Choose 0 to go back to previous menu: ")
						
  	
							match add_name_menu:
								case "0" :add_name = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "4" : 
						erase  = True
						while(erase):
							print("	Erase...")
							print(" 	0 -> Previous menu")
							erase_menu = input("Choose 0 to go back to previous menu: ")
						
  	
							match erase_menu:
								case "0" :erase = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "5" :
						edit = True
						while(edit):
							print("	Edit...")
							print(" 	0 -> Previous menu")
							edit_menu = input("Choose 0 to go back to previous menu: ")
						
  	
							match edit_menu:
								case "0" : edit = False
								case _ : print("	Invalid Input, Please go back to previous menu")
					case "6" : 
						assign_tone  = True
						while(assign_tone):
							print("	Assign Tone...")
							print(" 	0 -> Previous menu")
							assign_tone_menu = input("Choose 0 to go back to previous menu: ")
						
  	
							match assign_tone_menu:
								case "0" : assign_tone = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "7" :

						send_b_card  = True
						while(send_b_card):
							print("	Send b'card...")
							print(" 	0 -> Previous menu")
							send_b_card_menu = input("Choose 0 to go back to previous menu: ")
						
							match send_b_card_menu:
								case "0" :send_b_card= False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "8" : 
						options = """
						 Options
						1 -> Type of View
						2 -> Memory Status
						0 -> Previous menu


"""
						options_menu_going = True
						while(options_menu_going):
							print(options)
							options_menu = input("Choose from the above Options dropdown menu: ")
							match options_menu:
								case "1" : 
									type_of_view = True
									while(type_of_view):
										print("	Type of View...")
										print(" 	0 -> Previous menu")
										type_of_view_menu = input("Choose 0 to go back to previous menu: ")
						
										match type_of_view_menu :
											case "0" : type_of_view= False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "2" : 
									memory_status = True
									while(memory_status):
										print("	Memory Status...")
										print(" 	0 -> Previous menu")
										memory_status_menu = input("Choose 0 to go back to previous menu: ")
						
										match memory_status_menu: 
											case "0" : memory_status = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "0": options_menu_going = False
								case _ : print("Invalid Input")

					case "9" :
						speed_dials  = True
						while(speed_dials):
							print("	Speed dials...")
							print(" 	0 -> Previous menu")
							speed_dials_menu = input("Choose 0 to go back to previous menu: ")
						
							match speed_dials_menu:
								case "0" :speed_dials = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "10" : 

						voice_tag = True
						while(voice_tag):
							print("	Voice tag...")
							print(" 	0 -> Previous menu")
							voice_tag_menu = input("Choose 0 to go back to previous menu: ")
						
							match voice_tag_menu:
								case "0" :voice_tag= False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "0": phonebook_going = False
					case _ : print("Invalid Input")



		case "2" : 
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
				0 -> Previous menu


"""
			messages_menu_going = True
			while (messages_menu_going): 
				print(messages)
				messages_menu = input("Choose from the above Messages dropdown menu: ")
				match messages_menu:
					case "1" :
						write_messages = True
						while(write_messages):
							print("	Write messages...")
							print(" 	0 -> Previous menu")
							write_messages_menu = input("Choose 0 to go back to previous menu: ")
						
							match write_messages_menu:
								case "0" : write_messages= False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "2" : 
						inbox = True
						while(inbox):
							print("	Inbox...")
							print(" 	0 -> Previous menu")
							inbox_menu = input("Choose 0 to go back to previous menu: ")
						
							match inbox_menu:
								case "0" : inbox = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "3" : 
						outbox = True
						while(outbox):
							print("	Outbox...")
							print(" 	0 -> Previous menu")
							outbox_menu = input("Choose 0 to go back to previous menu: ")
						
							match outbox_menu:
								case "0" :outbox= False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "4" :
						picture_messages = True
						while(picture_messages):
							print("	Picture Messages...")
							print(" 	0 -> Previous menu")
							picture_messages_menu = input("Choose 0 to go back to previous menu: ")
						
							match picture_messages_menu:
								case "0" : picture_messages = False
								case _ : print("	Invalid Input, Please go back to previous menu")
					case "5" : 
						templates = True
						while(templates):
							print("	Templates...")
							print(" 	0 -> Previous menu")
							templates_menu = input("Choose 0 to go back to previous menu: ")
						
							match templates_menu:
								case "0" : templates= False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "6" : 
						smileys = True
						while(smileys):
							print("	Smileys...")
							print(" 	0 -> Previous menu")
							smileys_menu = input("Choose 0 to go back to previous menu: ")
						
							match smileys_menu:
								case "0" : smileys = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "7" :
						message_setting = """
						Messages Setting
						1 -> Set 1
						2 -> common
						0 -> Previous menu
"""
						message_setting_going = True
						while(message_setting_going):
							print(message_setting)
							message_setting_menu = input("Choose from the above Message settings dropdown menu: ")
							match message_setting_menu:
								case "1" :
									set_1 = """
									Set 1
									1 -> Message center number
									2 -> Messages sent as
									3 -> Message validity
									0 -> Previous menu

	
"""
									set_1_going = True
									while(set_1_going):
										print(set_1) 
										set_1_menu = input("Choose from the above Set 1 dropdown menu: ")
										match set_1_menu:
											case "1" : 
												message_center_number = True
												while(message_center_number):
													print("	Messages Center Number...")
													print(" 	0 -> Previous menu")
													message_center_number_menu = input("Choose 0 to go back to previous menu: ")
						
													match message_center_number_menu:
														case "0" : message_center_number = False
														case _ : print("	Invalid Input, Please go back to previous menu")
											case "2" : 
												message_sent_as = True
												while(message_sent_as):
													print("	Messages sent as...")
													print(" 	0 -> Previous menu")
													message_sent_as_menu = input("Choose 0 to go back to previous menu: ")
						
													match message_sent_as_menu:
														case "0" :message_sent_as = False
														case _ : print("	Invalid Input, Please go back to previous menu")

											case "3" : 
												message_validity = True
												while(message_validity):
													print("	Message validity...")
													print(" 	0 -> Previous menu")
													message_validity_menu = input("Choose 0 to go back to previous menu: ")
						
													match message_validity_menu:
														case "0" : message_validity = False
														case _ : print("	Invalid Input, Please go back to previous menu")

						
											case "0": set_1_going = False
											case _ : print("Invalid Input")


								case "2" : 
									common = """
									Common
									1 -> Delivery report
									2 -> Reply via same centre
									3 -> Character support
									0 -> Previous menu

	
"""
									common_going = True
									while(common_going):
										print(common) 
										common_menu = input("Choose from the above Common dropdown menu: ")
										match common_menu:
											case "1" : 
												delivery_report = True
												while(delivery_report):
													print("	Delivery report...")
													print(" 	0 -> Previous menu")
													delivery_report_menu = input("Choose 0 to go back to previous menu: ")
						
													match delivery_report_menu:
														case "0" : delivery_report = False
														case _ : print("	Invalid Input, Please go back to previous menu")

											case "2" : 
												reply_via_same_centre = True
												while(reply_via_same_centre):
													print("	Reply via same centre...")
													print(" 	0 -> Previous menu")
													reply_via_same_centre_menu = input("Choose 0 to go back to previous menu: ")
						
													match reply_via_same_centre_menu:
														case "0" : reply_via_same_centre = False
														case _ : print("	Invalid Input, Please go back to previous menu")

											case "3" :
												character_support = True
												while(character_support):
													print("	Character support...")
													print(" 	0 -> Previous menu")
													character_support_menu = input("Choose 0 to go back to previous menu: ")
						
													match character_support_menu:
														case "0" : character_support = False
														case _ : print("	Invalid Input, Please go back to previous menu")

											case "0": common_going = False
											case _ : print("Invalid Input")


								case "0" : message_setting_going = False
								case _ : print("Invalid Input")





					case "8" : 
						info_service = True
						while(info_service):
							print("	Info service...")
							print(" 	0 -> Previous menu")
							info_service_menu = input("Choose 0 to go back to previous menu: ")
						
							match info_service_menu:
								case "0" : info_service = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "9" : 
						voice_mailbox_number = True
						while(voice_mailbox_number):
							print("	Voice_mailbox_number...")
							print(" 	0 -> Previous menu")
							voice_mailbox_number_menu = input("Choose 0 to go back to previous menu: ")
						
							match voice_mailbox_number_menu:
								case "0" : voice_mailbox_number = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "10" : 
						service_command_editor = True
						while(service_command_editor):
							print("	Service command editor...")
							print(" 	0 -> Previous menu")
							service_command_editor_menu = input("Choose 0 to go back to previous menu: ")
						
							match service_command_editor_menu:
								case "0" : service_command_editor = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "0" : messages_menu_going = False
					case _ : print("Invalid Input")



			
		case "3" : print("Chat")
		case "4" : 
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
			0 -> Previous menu

		
			""";
			call_register_going = True
			while(call_register_going):
				print(call_register) 
				call_registe_menu = input("Choose from the above Call Register  dropdown menu: ")
				match call_registe_menu:
					case "1" : 
						missed_calls = True
						while(missed_calls):
							print("	Missed calls...")
							print(" 	0 -> Previous menu")
							missed_calls_menu = input("Choose 0 to go back to previous menu: ")
						
							match missed_calls_menu:
								case "0" : missed_calls = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "2" : 
						received_calls = True
						while(received_calls):
							print("	Received calls...")
							print(" 	0 -> Previous menu")
							received_calls_menu = input("Choose 0 to go back to previous menu: ")
						
							match received_calls_menu:
								case "0" : received_calls = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					
					case "3" :
						dialed_numbers = True
						while(dialed_numbers):
							print("	Dialed numbers...")
							print(" 	0 -> Previous menu")
							dialed_numbers_menu = input("Choose 0 to go back to previous menu: ")
						
							match dialed_numbers_menu:
								case "0" : dialed_numbers = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "4" : 
						erase_recent_call_lists = True
						while(erase_recent_call_lists):
							print("	Erase recent call lists...")
							print(" 	0 -> Previous menu")
							erase_recent_call_lists_menu = input("Choose 0 to go back to previous menu: ")
						
							match erase_recent_call_lists_menu:
								case "0" : erase_recent_call_lists = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "5" :
						show_call_duration = """
						Show call duration
						1 -> Last call duration
						2 -> All call's duration
						3 -> Recieved call's duration
						4 -> Dialed call duration
						5 -> Clear timer
						0 -> Previous menu

"""
						show_call_duration_going = True
						while(show_call_duration_going):
							print(show_call_duration)
							show_call_duration_menu = input("Choose from the above Show call duration drop down menu: ")
							match show_call_duration_menu:
								case "1" : 
									forward = True
									while(forward):
										print("	Last call duration...")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "2" :
									forward = True
									while(forward):
										print("	All call's duration...")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "3" :
									forward = True
									while(forward):
										print("	Last call duration...")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
								case "4" :
									forward = True
									while(forward):
										print("	Dialed call duration...")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
								case "5" :
									forward = True
									while(forward):
										print("	Clear timer...")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
				
								case "0" : show_call_duration_going = False
								case _ : print("Invalid Input")



					case "6" : 
						show_call_costs = """
						Show call costs
						1 -> Last call cost
						2 -> All call's cost											
						3 -> Clear counters
						0 -> Previous menu

"""
						show_call_costs_going = True
						while(show_call_costs_going):
							print(show_call_costs)
							show_call_costs_menu = input("Choose from the above Show call Costs dropdown menu: ")
							match show_call_costs_menu:
								case "1" : 
									forward = True
									while(forward):
										print("	Last call costs...")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
								case "2" :
									forward = True
									while(forward):
										print("	All call's cost...")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
								case "3" : 
									forward = True
									while(forward):
										print("	Clear counters...")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")


								case "0" : show_call_costs_going = False
								case _ : print("Invalid Input")


				
					case "7" :
						call_cost_settings = """
						Call cost settings
						1 -> call cost limit
						2 -> Show costs in
						0 -> Previous menu
					
"""
						call_cost_settings_going = True
						while(call_cost_settings_going):
							print(call_cost_settings);
							call_cost_settings = input("Choose from the above Call cost settings dropdown menu: ")
							match call_cost_settings:
								case "1":
									print(" 	Call costs limit") 
									print("		0 -> Go back")
								case "2" :
									forward = True
									while(forward):
										print("	Show costs in...")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")


								case "0" : call_cost_settings_going = False
								case _ : print("Invalid Input")


					case "8" :
						forward = True
						while(forward):
							print("	Prepaid credit...")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")
					case "0": call_register_going = False
					case _ : print("Invalid Input")





		case "5" :
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
			0 -> Previous menu

"""
			tones_menu_going = True
			while(tones_menu_going):
				print(tones)
				tones_menu = input("Choose from the above Tones dropdown menu: ")
				match tones_menu:
					case "1" :
						forward = True
						while(forward):
							print("	Ringing tone")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "2" :
						forward = True
						while(forward):
							print("	Ringing volume")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "3" :
						forward = True
						while(forward):
							print("	Ringing volume")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "4" : 
						forward = True
						while(forward):
							print("Incoming call alert")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")
					case "5" :
						forward = True
						while(forward):
							print("	Message alert tones")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")
					case "6" : 
						forward = True
						while(forward):
							print("	Keypad tones")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")
					case "7" :
						forward = True
						while(forward):
							print("	Warning and game tones")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "8" : 
						forward = True
						while(forward):
							print("	Vibrating alert")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "9" : 
						forward = True
						while(forward):
							print("	Screen saver")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")



					case "0" : tones_menu_going = False
					case _ : print("Invalid Input")





		case "6" : 
			settings = """
				Settings
				1 -> Call Settings
				2 -> Phone settings
				3 -> Security settings
				4 -> Restore Factory Settings
				0 -> Previous menu

			
"""
			setting_menu_going = True
			while(setting_menu_going):
				print(settings)
				settings_menu = input("Choose from the above Settings dropdown menu: ")
				match settings_menu:
					case "1" : 
						call_setting = """
						Call Setting
						1 -> Automatic redial
						2 -> Speed dialing
						3 -> Call waiting options
						4 -> Own number sending
						5 -> Phone line in use
						6 -> Automatic answer
						0 -> Previous menu

"""
						
						call_setting_going = True
						while(call_setting_going):
							print(call_setting );
							call_setting_menu = input("Choose from the above Call settings dropdown menu: ")
							match call_setting_menu:
								case "1" :
									forward = True
									while(forward):
										print("	Automatic redial")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")


								case "2" :
									forward = True
									while(forward):
										print("	Speed dialing")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")


								case "3" :
									forward = True
									while(forward):
										print("	Call waiting options")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
								case "4" :
									forward = True
									while(forward):
										print("	Own number sending")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
								case "5" : 
									forward = True
									while(forward):
										print("	Phone line in use")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "6" :
									forward = True
									while(forward):
										print("	Automatic answer")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "0" : call_setting_going = False
								case _ : print("Invalid Input")


					case "2" : 
						phone_setting = """
						Phone Setting
						1 -> Language
						2 -> Cell info display
						3 -> Welcome note
						4 -> Network selection
						5 -> Lights
						6 -> Confirm SIM service actions
						0 -> Previous menu

"""

						phone_setting_going = True
						while(phone_setting_going):
							print(phone_setting );
							phone_setting_menu = input("Choose from the above Phone settings dropdown menu: ")
							match phone_setting_menu:
								case "1" :
									forward = True
									while(forward):
										print("	Language")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "2" : 
									forward = True
									while(forward):
										print("	Cell info display")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "3" : 
									forward = True
									while(forward):
										print("	 Welcome note")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "4" : 
									forward = True
									while(forward):
										print("	 Network selection")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
			 
						

								case "5" : 
									forward = True
									while(forward):
										print("	 Lights")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "6" : 
									forward = True
									while(forward):
										print("	 Confirm SIM service actions")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
								case "0" : phone_setting_going = False
								case _ : print("Invalid Input")



					case "3" : 
						security_setting = """
						Security Setting
						1 -> Pin code request
						2 -> Call barring service
						3 -> Fixed dialing
						4 -> Closed user group
						5 -> Phone security
						6 -> Change access codes
						0 -> Previous menu

"""


						security_setting_going = True
						while(security_setting_going):
							print(security_setting);
							security_setting_menu = input("Choose from the above Security settings dropdown menu: ")
							match security_setting_menu:
								case "1" :
									forward = True
									while(forward):
										print("		Pin code request")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
 
								case "2" : 
									forward = True
									while(forward):
										print("		Call barring service")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
								case "3" : 
									forward = True
									while(forward):
										print("	Fixed dialing")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")


								case "4" : 
									forward = True
									while(forward):
										print("	Closed user group")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "5" :
									forward = True
									while(forward):
										print("	Phone security")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")
								case "6" : 
									forward = True
									while(forward):
										print("	 Change access codes")
										print(" 	0 -> Previous menu")
										choose = input("Choose 0 to go back to previous menu: ")
						
										match choose:
											case "0" : forward = False
											case _ : print("	Invalid Input, Please go back to previous menu")

								case "0" : security_setting_going = False
								case _ : print("Invalid Input")

					case "4":
						forward = True
						while(forward):
							print("	Restore Factory Settings")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "0": setting_menu_going = False
					case _ : print("Invalid Input")






		case "7" :
			forward = True
			while(forward):
				print("	Call divert")
				print(" 	0 -> Previous menu")
				choose = input("Choose 0 to go back to previous menu: ")
						
				match choose:
					case "0" : forward = False
					case _ : print("	Invalid Input, Please go back to previous menu")


		case "8" : 
			forward = True
			while(forward):
				print("	Games")
				print(" 	0 -> Previous menu")
				choose = input("Choose 0 to go back to previous menu: ")
						
				match choose:
					case "0" : forward = False
					case _ : print("	Invalid Input, Please go back to previous menu")

		case "9" : 
			forward = True
			while(forward):
				print("	Calculator")
				print(" 	0 -> Previous menu")
				choose = input("Choose 0 to go back to previous menu: ")
						
				match choose:
					case "0" : forward = False
					case _ : print("	Invalid Input, Please go back to previous menu")


		case "10" : 
			forward = True
			while(forward):
				print("	Remainders")
				print(" 	0 -> Previous menu")
				choose = input("Choose 0 to go back to previous menu: ")
						
				match choose:
					case "0" : forward = False
					case _ : print("	Invalid Input, Please go back to previous menu")


		case "11" : 
			clock = """
			Clock  
			1 -> Alarm clock
			2 -> Clock settings
			3 -> Date setting
			4 -> Stopwatch
			5 -> Countdown timer
			6 -> Auto update of date and time
			0 -> Previous menu

"""
			clock_menu_going = True
			while(clock_menu_going):
				print(clock)
				clock_menu = input("Choose from the above Clock dropdown menu: ")
				match clock_menu:
					case "1" : 
						forward = True
						while(forward):
							print("	Alarm clock")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")



					case "2" : 
						forward = True
						while(forward):
							print("	Clock settings")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "3" : 
						forward = True
						while(forward):
							print("	Date setting")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")
					case "4" : 
						forward = True
						while(forward):
							print("	Stopwatch")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "5" : 
						forward = True
						while(forward):
							print("	Countdown timer")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")

					case "6" :
						forward = True
						while(forward):
							print("	Auto update of date and time")
							print(" 	0 -> Previous menu")
							choose = input("Choose 0 to go back to previous menu: ")
						
							match choose:
								case "0" : forward = False
								case _ : print("	Invalid Input, Please go back to previous menu")


					case "0" : clock_menu_going = False
					case _ : print("Invalid Input")


		

		case "12" : 
			forward = True
			while(forward):
				print("	Profiles")
				print(" 	0 -> Previous menu")
				choose = input("Choose 0 to go back to previous menu: ")
						
				match choose:
					case "0" : forward = False
					case _ : print("	Invalid Input, Please go back to previous menu")
		case "13" : 
			forward = True
			while(forward):
				print("	Sim settings")
				print(" 	0 -> Previous menu")
				choose = input("Choose 0 to go back to previous menu: ")
						
				match choose:
					case "0" : forward = False
					case _ : print("	Invalid Input, Please go back to previous menu")

		case "0": menu_display_going = False
		case _ : print("Invalid Input")


