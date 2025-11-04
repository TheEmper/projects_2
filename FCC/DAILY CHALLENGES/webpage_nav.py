def navigate(commands):
    current_page = "Home"
    back_history = []     
    forward_history = []   
    
    for command in commands:
        if "Visit" in command:
            # Extract page name (everything after "Visit ")
            page_name = command.split()
            page_name = " ".join(page_name[1::])
            
            back_history.append(current_page)
            
            current_page = page_name
            
            forward_history = []
            
        elif command == "Back":
            if back_history:
                # Save current page to forward history
                forward_history.append(current_page)
                
                # Go back to previous page
                current_page = back_history.pop()
        
        elif command == "Forward":
            if forward_history:
                # Save current page to back history
                back_history.append(current_page)
                
                # Go forward
                current_page = forward_history.pop()
    
    return current_page

print(navigate(["Visit About Us", "Visit Visit Us", "Forward", "Visit Contact Us", "Back"]))