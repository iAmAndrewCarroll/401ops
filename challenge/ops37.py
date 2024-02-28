#!/usr/bin/env python3

import requests
import webbrowser

# Target site URL
targetsite = "http://www.whatarecookies.com/cookietest.asp"

# Function to send cookie back to the site and capture HTTP response
def send_cookie_and_capture_response(cookie):
    # Send GET request with the cookie
    response = requests.get(targetsite, cookies=cookie)
    # Generate HTML file to capture response content
    with open("response.html", "w") as html_file:
        html_file.write(response.text)
    # Open HTML file in Firefox
    webbrowser.open("response.html")

# Function to capture cookie from the target site
def capture_cookie():
    # Send GET request to the target site
    response = requests.get(targetsite)
    # Capture the cookie from the response
    cookie = response.cookies
    return cookie

# Main function
def main():
    print("Target site is " + targetsite)
    # Capture the cookie
    cookie = capture_cookie()
    print("Captured cookie:", cookie)
    # Send the cookie back to the site and capture HTTP response
    send_cookie_and_capture_response(cookie)

if __name__ == "__main__":
    main()
