from transformers import pipeline

classifier = pipeline("sentiment-analysis")
answer = classifier(
  [
    "I've been waiting for this my whole life.",
    "This sucks!",
  ]
)

print(answer)