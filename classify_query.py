# classify_query.py

def classify_query(user_input):
    if "available" in user_input.lower():
        return "availability"
    elif "recommend" in user_input.lower() or "suggest" in user_input.lower():
        return "recommendation"
    elif "price" in user_input.lower() or "cost" in user_input.lower():
        return "details"
    else:
        return "general"
