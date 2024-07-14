def print_scenario(scenario):
    print("\n" + scenario['question'])
    for idx, option in enumerate(scenario['options'], 1):
        print(f"{idx}. {option}")

def get_user_choice():
    while True:
        try:
            choice = int(input("Your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")

def main():
    scenarios = [
        {
            'question': "You receive an email from your bank asking you to update your password via a link. What do you do?",
            'options': [
                "Click the link and update your password.",
                "Ignore the email.",
                "Report the email to your bank.",
                "Reply to the email asking for more information."
            ],
            'correct': 3,
            'explanation': "Banks usually do not ask for sensitive information via email. It's best to report such emails directly to your bank."
        },
        {
            'question': "A colleague asks for your login credentials to access a shared document. What do you do?",
            'options': [
                "Give them your credentials since they are a colleague.",
                "Tell them to request access through the proper channels.",
                "Share the document via email.",
                "Ignore the request."
            ],
            'correct': 2,
            'explanation': "Never share your login credentials. Direct your colleague to the proper access request channels."
        },
        {
            'question': "You receive a friend request on social media from someone you don't know, but they are friends with several of your colleagues. What do you do?",
            'options': [
                "Accept the request because you have mutual connections.",
                "Ignore the request.",
                "Send a message to find out how they know your colleagues.",
                "Report the profile to the social media platform."
            ],
            'correct': 2,
            'explanation': "It's safer to ignore friend requests from people you don't know, even if you have mutual connections. This could be a tactic to gather information about you."
        },
        {
            'question': "While browsing, a pop-up appears claiming your computer is infected and urging you to download an antivirus tool. What do you do?",
            'options': [
                "Download and install the tool immediately.",
                "Close the pop-up and run your existing antivirus software.",
                "Ignore the pop-up.",
                "Click the pop-up to get more information."
            ],
            'correct': 2,
            'explanation': "Close the pop-up and run your existing antivirus software. Pop-ups like these are often scams trying to install malware on your computer."
        },
        {
            'question': "You get a phone call from someone claiming to be from IT support, asking for your login details to fix an issue. What do you do?",
            'options': [
                "Give them your login details to resolve the issue quickly.",
                "Hang up and report the call to your IT department.",
                "Ask them to call back later.",
                "Verify their identity by asking for their employee ID."
            ],
            'correct': 2,
            'explanation': "Always hang up and report suspicious calls to your IT department. IT support should never ask for your login details over the phone."
        },
        {
            'question': "You notice a USB drive labeled 'Confidential' in the office parking lot. What do you do?",
            'options': [
                "Plug it into your computer to see what's on it.",
                "Give it to your manager or IT department.",
                "Leave it where it is.",
                "Take it home and check it on your personal computer."
            ],
            'correct': 2,
            'explanation': "Always give unknown USB drives to your manager or IT department. They could contain malware or be part of a targeted attack."
        },
        {
            'question': "You receive a text message from your CEO urgently asking for sensitive company information. What do you do?",
            'options': [
                "Respond with the requested information immediately.",
                "Ignore the message.",
                "Verify the request by calling the CEO's known phone number.",
                "Report the message to your IT department."
            ],
            'correct': 3,
            'explanation': "Verify any urgent or sensitive requests through known channels before responding. This could be a targeted phishing attempt."
        },
        {
            'question': "An online survey offers a chance to win a prize in exchange for personal information. What do you do?",
            'options': [
                "Complete the survey with accurate information.",
                "Complete the survey with fake information.",
                "Ignore the survey.",
                "Report the survey to the website administrator."
            ],
            'correct': 3,
            'explanation': "Ignore such surveys as they often aim to collect personal information for malicious purposes. Legitimate surveys usually don't offer prizes for personal details."
        },
        {
            'question': "A coworker asks you to click a link to a 'funny video' on their personal blog. What do you do?",
            'options': [
                "Click the link to watch the video.",
                "Ask them to send the video in another format.",
                "Check the link for any signs of malicious content.",
                "Report the link to your IT department."
            ],
            'correct': 3,
            'explanation': "Always check links for signs of malicious content before clicking, even if they come from coworkers. It's possible their account has been compromised."
        },
        {
            'question': "You find a document on a shared drive that appears to contain sensitive information. What do you do?",
            'options': [
                "Read the document to see if it concerns you.",
                "Delete the document.",
                "Report the document to your manager or IT department.",
                "Move the document to a more secure location."
            ],
            'correct': 3,
            'explanation': "Report any sensitive information found in unexpected locations to your manager or IT department. Handling it yourself could lead to data breaches."
        }
    ]

    print("Welcome to the Social Engineering Awareness Quiz by Rayyan Afridi!")
    score = 0

    for scenario in scenarios:
        print_scenario(scenario)
        choice = get_user_choice()

        if choice == scenario['correct']:
            print("Correct! " + scenario['explanation'])
            score += 1
        else:
            print("Incorrect. " + scenario['explanation'])

    print(f"\nYour total score: {score}/{len(scenarios)}")
    print("Thank you for taking the Social Engineering Awareness Quiz by Rayyan Afridi!")

if __name__ == "__main__":
    main()
