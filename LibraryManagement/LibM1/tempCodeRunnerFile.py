        try:
            role_input = int(input("select the Role: "))
            if role_input ==1:
                return "User"
            if role_input ==2:
                return "Admin"
            
            if not role_input:
                print("\n Please select a valid role")
        except ValueError:
            print(f"\n Role Error: {ValueError}")
