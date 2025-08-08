def replace_author_name_email(name, email):
    old_name = b"Prabin Magar"
    old_email = b"psmagar123451@gmail.com"

    new_name = b"Prashant Yadav"
    new_email = b"prashantyadav22277@gmail.com"

    if name == old_name or email == old_email:
        return new_name, new_email
    return name, email
