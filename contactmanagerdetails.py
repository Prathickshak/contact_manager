import streamlit as st

# Define functions for each operation

def display_menu():
    st.sidebar.title("Contact Management Menu")
    menu = ["View Contacts", "Add a New Contact", "Search for a Contact", "Delete a Contact", "Exit"]
    choice = st.sidebar.radio("Select an option:", menu, key="menu")
    return choice

def view_contacts(contacts):
    st.write("### Contact List")
    if contacts:
        for name, phone in contacts.items():
            st.write(f"**{name}**: {phone}")
    else:
        st.write("No contacts available.")

def add_contact(contacts):
    st.write("### Add a New Contact")
    name = st.text_input("Enter contact name", key="name")
    phone = st.text_input("Enter contact phone number", key="phone")
    if st.button("Add Contact"):
        if name and phone:
            contacts[name] = phone
            st.success(f"Contact {name} added successfully.")
        else:
            st.error("Please provide both name and phone number.")

def search_contact(contacts):
    st.write("### Search for a Contact")
    name = st.text_input("Enter contact name to search", key="search_name")
    if st.button("Search"):
        if name in contacts:
            st.write(f"**{name}**: {contacts[name]}")
        else:
            st.error("Contact not found.")

def delete_contact(contacts):
    st.write("### Delete a Contact")
    name = st.text_input("Enter contact name to delete", key="delete_name")
    if st.button("Delete"):
        if name in contacts:
            del contacts[name]
            st.success(f"Contact {name} deleted successfully.")
        else:
            st.error("Contact not found.")

def main():
    st.title("Simple Contact Management System")

    # Initialize contacts dictionary
    if 'contacts' not in st.session_state:
        st.session_state.contacts = {}

    contacts = st.session_state.contacts

    choice = display_menu()

    if choice == "View Contacts":
        view_contacts(contacts)
    elif choice == "Add a New Contact":
        add_contact(contacts)
    elif choice == "Search for a Contact":
        search_contact(contacts)
    elif choice == "Delete a Contact":
        delete_contact(contacts)
    elif choice == "Exit":
        st.write("Exiting...")

if __name__ == "__main__":
    main()