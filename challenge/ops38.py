#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin
from tqdm import tqdm  # Import tqdm for the progress bar

# Function to get all forms on a webpage
def get_all_forms(url):
    """
    Retrieve all forms present on the given webpage URL.
    
    Args:
        url (str): The URL of the webpage to scan.
    
    Returns:
        bs4.ResultSet: A ResultSet containing all forms found on the webpage.
    """
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

# Function to get details of a form
def get_form_details(form):
    """
    Retrieve details of a specific form.
    
    Args:
        form (bs4.element.Tag): The form element to extract details from.
    
    Returns:
        dict: A dictionary containing details of the form, including action, method, and inputs.
    """
    details = {}
    action = form.attrs.get("action", "").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

# Function to submit form data
def submit_form(form_details, url, value):
    """
    Submit form data with a specific value to the target URL.
    
    Args:
        form_details (dict): Details of the form to submit data to.
        url (str): The URL of the target webpage.
        value (str): The value to be submitted.
    
    Returns:
        requests.models.Response: The response object after form submission.
    """
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value
    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

# Function to scan for XSS vulnerabilities
def scan_xss(url):
    """
    Scan a webpage for XSS vulnerabilities.
    
    Args:
        url (str): The URL of the webpage to scan.
    
    Returns:
        tuple: A tuple containing logging information and vulnerability detection details.
    """
    forms = get_all_forms(url)
    log_info = f"[+] Detected {len(forms)} forms on {url}."
    js_script = '<script>alert("XSS Vulnerability Detected!");</script>'
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            vuln_info = f"[+] XSS Detected on {url}\n[*] Form details:\n{form_details}"
            is_vulnerable = True
            return log_info, vuln_info
    return log_info, ""

# Function to export data to a file
def export_to_file(log_info, vuln_info):
    """
    Export logging information and vulnerability detection details to a text file.
    
    Args:
        log_info (str): Logging information to be exported.
        vuln_info (str): Vulnerability detection details to be exported.
    """
    while True:
        filename = input("Enter the filename: ")
        if not filename.endswith(".txt"):
            filename += ".txt"  # Add .txt extension if not present
        
        if os.path.exists(filename):
            choice = input("File already exists. Do you want to overwrite it? (yes/no): ")
            if choice.lower() == "yes" or choice.lower() == "y":
                break
            else:
                continue
        else:
            break
    
    with open(filename, 'w') as file:
        file.write("Logging Information:\n")
        file.write(log_info + "\n\n")  # Write logging information
        if vuln_info:
            file.write("Vulnerability Detection Details:\n")
            file.write(vuln_info)  # Write vulnerability detection details
            file.write("\n")  # Add a newline after vulnerability detection details

            # Add explanations for the log findings
            file.write("Explanation:\n")
            file.write("- XSS stands for Cross-Site Scripting. It's a security vulnerability typically found in web applications.")
            file.write("\n")
        else:
            file.write("Explanation:\n")
            file.write("- No XSS vulnerabilities detected.")
            file.write("\n")

    # Get the size of the written file
    file_size = os.path.getsize(filename)
    
    # Initialize tqdm progress bar with the file size
    with tqdm(total=file_size, unit="B", unit_scale=True, desc="Exporting", leave=True) as pbar:
        pbar.update(file_size)  # Update progress bar to completion
    print("Data exported successfully.")

# Main function
if __name__ == "__main__":
    while True:
        print("Choose an option:")
        print("1. Positive URL: https://xss-game.appspot.com/level1/frame")
        print("2. Negative URL: http://dvwa.local/login.php")
        print("3. Enter a different URL")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")
        if choice == "1":
            url = "https://xss-game.appspot.com/level1/frame"
        elif choice == "2":
            url = "http://dvwa.local/login.php"
        elif choice == "3":
            url = input("Enter the URL: ")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose again.")
            continue
        
        print("Scanning for XSS vulnerabilities...")
        log_info, vuln_info = scan_xss(url)
        if vuln_info:
            print(vuln_info)
        
        export_choice = input("Do you want to export the data to a file? (yes/no): ")
        if export_choice.lower() == "yes" or export_choice.lower() == "y":
            export_to_file(log_info, vuln_info)
        
        new_scan = input("Do you want to start a new scan? (yes/no): ")
        if new_scan.lower() == "no" or new_scan.lower() == "n":
            break
