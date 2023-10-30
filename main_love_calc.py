# Print a message to let the user know the Love Calculator is working
print("The Love Calculator is calculating your score...")

# Take user input for two names
name1 = input("What is your name? ")  # Asking the first person for their name
name2 = input(
    "What is their name? ")  # Asking the second person for their name


# Define a function to calculate the love score
def love_score(name1, name2):
  # Combine the names and convert to lowercase for case-insensitive comparison
  combined_names = (name1 + name2).lower()

  # Count the occurrences of letters in 'TRUE' in the combined names
  true_count = sum(combined_names.count(letter) for letter in "true")

  # Count the occurrences of letters in 'LOVE' in the combined names
  love_count = sum(combined_names.count(letter) for letter in "love")

  # Combine the counts to create a two-digit score
  score = int(str(true_count) + str(love_count))

  # Initialize the message with a default score announcement
  message = f"Your score is {score}."

  # Check for special cases to update the message accordingly
  if score < 10 or score > 90:
    message = f"Your score is {score}, you go together like coke and mentos."
  if 40 <= score <= 50:
    message = f"Your score is {score}, you are alright together."

  # Return the final message
  return message


# Main execution: Calculate and print the love score based on user input
if __name__ == "__main__":
  print(love_score(name1, name2))
