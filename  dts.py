import requests

import os

import re

import time

import random

from requests.exceptions import RequestException



# Function to clear the terminal screen

def clear_screen():

    os.system("clear")



# Function to set up the cookie

def set_cookie():

    Cookie = input("\033[92mEnter Your Cookie :: ")

    return Cookie



# Function to prompt for commenter's name

def get_commenter_name():

    return input("\033[92mEnter Hater Name :: ")



# Function to prompt for password

def get_password():

    return input("\033[92mEnter Password :: ")



# Function to handle network requests

def make_request(url, headers, cookies):

    try:

        response = requests.get(url, headers=headers, cookies=cookies).text

        return response

    except RequestException as e:

        print("\033[91m[!] Error making request:", e)  # Bright Red color for errors

        return None



# Logo

clear_screen()

logo ="""
 
                   
\033[1;35mRRRRRRRRRRRRRRRRR   EEEEEEEEEEEEEEEEEEEEEEBBBBBBBBBBBBBBBBB   EEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLL                SSSSSSSSSSSSSSS 
\033[1;45mR::::::::::::::::R  E::::::::::::::::::::EB::::::::::::::::B  E::::::::::::::::::::EL:::::::::L              SS:::::::::::::::S
\033[1;36mR::::::RRRRRR:::::R E::::::::::::::::::::EB::::::BBBBBB:::::B E::::::::::::::::::::EL:::::::::L             S:::::SSSSSS::::::S
\033[1;37mRR:::::R     R:::::REE::::::EEEEEEEEE::::EBB:::::B     B:::::BEE::::::EEEEEEEEE::::ELL:::::::LL             S:::::S     SSSSSSS
 \033[1;34m R::::R     R:::::R  E:::::E       EEEEEE  B::::B     B:::::B  E:::::E       EEEEEE  L:::::L               S:::::S            
  \033[1;33mR::::R     R:::::R  E:::::E               B::::B     B:::::B  E:::::E               L:::::L               S:::::S            
  \033[1;32mR::::RRRRRR:::::R   E::::::EEEEEEEEEE     B::::BBBBBB:::::B   E::::::EEEEEEEEEE     L:::::L                S::::SSSS         
  \033[1;31mR:::::::::::::RR    E:::::::::::::::E     B:::::::::::::BB    E:::::::::::::::E     L:::::L                 SS::::::SSSSS    
  \033[1;39mR::::RRRRRR:::::R   E:::::::::::::::E     B::::BBBBBB:::::B   E:::::::::::::::E     L:::::L                   SSS::::::::SS  
  \033[1;35mR::::R     R:::::R  E::::::EEEEEEEEEE     B::::B     B:::::B  E::::::EEEEEEEEEE     L:::::L                      SSSSSS::::S 
  \033[1;38mR::::R     R:::::R  E:::::E               B::::B     B:::::B  E:::::E               L:::::L                           S:::::S
  \033[1;42mR::::R     R:::::R  E:::::E       EEEEEE  B::::B     B:::::B  E:::::E       EEEEEE  L:::::L         LLLLLL            S:::::S
\033[1;39mRR:::::R     R:::::REE::::::EEEEEEEE:::::EBB:::::BBBBBB::::::BEE::::::EEEEEEEE:::::ELL:::::::LLLLLLLLL:::::LSSSSSSS     S:::::S
\033[1;33mR::::::R     R:::::RE::::::::::::::::::::EB:::::::::::::::::B E::::::::::::::::::::EL::::::::::::::::::::::LS::::::SSSSSS:::::S
\033[1;45mR::::::R     R:::::RE::::::::::::::::::::EB::::::::::::::::B  E::::::::::::::::::::EL::::::::::::::::::::::LS:::::::::::::::SS 
\033[1;48mRRRRRRRR     RRRRRRREEEEEEEEEEEEEEEEEEEEEEBBBBBBBBBBBBBBBBB   EEEEEEEEEEEEEEEEEEEEEELLLLLLLLLLLLLLLLLLLLLLLL SSSSSSSSSSSSSSS   
                                                                                                                               

        
                                                                                                                               
 \x1b[1;33m════════════════════════════════════════════════════════

\033[1;34m▇➤ 😘𝑶𝑵𝑾𝑬𝑹             : 𝑹𝑶𝑴𝑰 →→→→▇➤ 😘

\033[1;35m▇➤🙃 𝑨𝑫𝑫𝑴𝑰𝑵               :  𝑯𝑨𝑴𝒁𝑰𝑰 𝑿 𝑹𝑬𝑯𝑴𝑨𝑵 𝑿 𝑼𝑺𝑨𝑴𝑨→→→▇➤🙃

\033[1;36m▇➤ 😁𝐑𝐔𝐋𝐄𝐗                 : 𝑹𝒆𝒃𝒆𝒍𝒔  ▇➤🙂

\033[1;33m▇➤ 😘𝐅𝐀𝐂𝐄𝐁𝐎𝐎𝐊              : Ｒｏｍｉ  ▇➤😉

\x1b[1;34m════════════════════════════════════════════════════════

\033[1;36m          𝑴𝑬𝑴𝑩𝑬𝑹 Δ>     🍒 Sammy x Aitzaz x kashi x faseeh x Vicky🍒

"""







print(logo)



# Start time

print("\033[92mStart Time:", time.strftime("%Y-%m-%d %H:%M:%S"))  



# Login System




while True:

    try:

        print()

        cookies = set_cookie()



        response = make_request('https://business.facebook.com/business_locations', headers={

            'Cookie': cookies,

            'User-Agent': 'Mozilla/5.0 (Linux; Android 11; RMX2144 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/375.1.0.28.111;]'

        }, cookies={'Cookie': cookies})



        if response is None:

            break



        token_eaag = re.search('(EAAG\w+)', str(response)).group(1)

        id_post = int(input("\033[92mEnter Post Id :: "))

        commenter_name = get_commenter_name() 

        delay = int(input("\033[92mEnter Delay (Second) :: "))  # Bright Green color for input prompt

        comment_file_path = input("\033[92mEnter Your Comment File Path :: ")  # Bright Green color for input prompt



        # Reading comments from the file

        with open(comment_file_path, 'r') as file:

            comments = file.readlines()



        x, y = 0, 0

        print()



        while True:

            try:

                time.sleep(delay)

                teks = comments[x].strip()

                comment_with_name = f"{commenter_name}: {teks}"  # Add commenter's name to the comment

                data = {

                    'message': comment_with_name,

                    'access_token': token_eaag

                }

                response2 = requests.post(f'https://graph.facebook.com/{id_post}/comments/', data=data, cookies={'Cookie': cookies}).json()

                if '\'id\':' in str(response2):

                    print("\033[92mPost id ::", id_post)  # Post ID

                    print("\033[92mDate time ::", time.strftime("%Y-%m-%d %H:%M:%S"))  # Date time

                    print("\033[92mComment sent ::", comment_with_name)  # Comment sent with name

                    print('\033[97m' + '──────────────────────────────────────────────────────────────')  # Additional line in bright white color

                    x = (x + 1) % len(comments)  # Move to the next comment

                else:

                    y += 1

                    print("\033[91m[{}] Status : Failure".format(y))  # Bright Red color for failure message

                    print("\033[91m[/]Link : https://m.basic.facebook.com//{}".format(id_post))  # Bright Red color for failure message

                    print("\033[91m[/]Comments : {}\n".format(comment_with_name))  # Bright Red color for failure message

                    continue



            except RequestException as e:

                print("\033[91m[!] Error making request:", e)  # Bright Red color for errors

                time.sleep(5.5)

                continue



    except Exception as e:

        print("\033[91m[!] An unexpected error occurred:", e)  # Bright Red color for errors

        break