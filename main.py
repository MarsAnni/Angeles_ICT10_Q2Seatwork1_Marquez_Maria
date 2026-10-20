from pyscript import document

club_members = [ # list of the members... looks veryyy familiar
    "Annika Naguit",
    "Brielle Marquez",
    "Maria Frigillana",
    "David Pekson",
]

def check_member(e):
    first_name = document.getElementById("first_name").value.strip().title()
    last_name = document.getElementById("last_name").value.strip().title()
    full_name = first_name + " " + last_name # combines the two names
    is_member = full_name in club_members # checks if true or false after combininig
    messages = { # messages for both possible results
        True: f"congratulations, {full_name}! youre so from here!",
        False: f"sooo sorry, {full_name}... youre not from here!"
    }
    document.getElementById("result").innerHTML = messages[is_member]