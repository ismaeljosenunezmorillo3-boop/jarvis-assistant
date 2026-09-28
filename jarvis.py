#!/usr/bin/env python3
"""
JARVIS Assistant - A voice-controlled AI assistant for your computer
"""

import os
import sys
import json
import datetime
import subprocess
import webbrowser
from typing import Optional, Dict, Any

try:
    import speech_recognition as sr
    import pyttsx3
except ImportError:
    print("Error: Required libraries not installed. Run: pip install -r requirements.txt")
    sys.exit(1)


class JARVISAssistant:
    """Main JARVIS Assistant class"""
    
    def __init__(self):
        """Initialize JARVIS Assistant"""
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        self.is_running = False
        self.commands = self._load_commands()
        
    def speak(self, text: str):
        """Speak the given text"""
        print(f"JARVIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen(self) -> Optional[str]:
        """Listen and recognize speech"""
        try:
            with sr.Microphone() as source:
                print("Listening...")
                self.recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, timeout=10)
                
            text = self.recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            self.speak("I didn't understand that. Please repeat.")
            return None
        except sr.RequestError:
            self.speak("Unable to reach the speech recognition service.")
            return None
        except Exception as e:
            print(f"Error listening: {e}")
            return None
            
    def _load_commands(self) -> Dict[str, str]:
        """Load commands from config file"""
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        if os.path.exists(config_path):
            with open(config_path, 'r') as f:
                return json.load(f).get('commands', {})
        return {}
        
    def process_command(self, command: str) -> bool:
        """Process voice command"""
        if not command:
            return True
            
        # Time commands
        if 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            self.speak(f"The current time is {current_time}")
            return True
            
        # Date commands
        if 'date' in command:
            current_date = datetime.datetime.now().strftime('%A, %B %d, %Y')
            self.speak(f"Today is {current_date}")
            return True
            
        # Open browser
        if 'open' in command and 'browser' in command:
            self.speak("Opening browser")
            webbrowser.open('https://www.google.com')
            return True
            
        # Google search
        if 'search' in command:
            search_term = command.replace('search', '').strip()
            self.speak(f"Searching for {search_term}")
            webbrowser.open(f'https://www.google.com/search?q={search_term}')
            return True
            
        # Exit commands
        if any(word in command for word in ['exit', 'quit', 'goodbye', 'bye']):
            self.speak("Goodbye, Sir. It has been a pleasure serving you.")
            return False
            
        # Help command
        if 'help' in command:
            self.speak("I can help you with time, date, opening the browser, and searching the web.")
            return True
            
        self.speak("Command not recognized. Say help for available commands.")
        return True
        
    def run(self):
        """Start JARVIS Assistant"""
        self.is_running = True
        self.speak("Good morning, Sir. JARVIS online and ready to serve.")
        
        while self.is_running:
            command = self.listen()
            if command:
                self.is_running = self.process_command(command)
                
        self.speak("System shutting down.")


def main():
    """Main entry point"""
    jarvis = JARVISAssistant()
    try:
        jarvis.run()
    except KeyboardInterrupt:
        jarvis.speak("System interrupted. Shutting down.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
