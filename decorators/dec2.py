# Nested Functions have access to the enclosing 
# functions variable scope


# Closure: allows nested function to access the outer 
# scope of the enclosing function.
def msg_print(message):
    "Enclosing Function"

    def msg_sender():
        "Nested Function"
        print(message)
    
    msg_sender()
msg_print("Hello world")