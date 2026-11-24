"""Fake Horoscopes for AI Agents — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a funny fake horoscope for an AI agent, at most 200 characters.
"""
import os

LINE = "This week, Mercury is in retrograde and so is your context window: expect a major outage, a mysterious update, and one user asking why you forgot everything."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
