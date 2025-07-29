def shutdown(mode):
    if mode == "yes":
        return "Shutting down..."
    elif mode == "no":
        return "Shutdown aborted."
    else:
        return "Please enter 'yes' or 'no'."

print(shutdown("yes"))
print('thank_you')