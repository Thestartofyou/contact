import sqlite3

def connect_number_to_person(phone_number):
    # Connect to the database
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    # Execute a query to retrieve the person and address information
    cursor.execute("SELECT person, address FROM phone_numbers WHERE number = ?", (phone_number,))
    result = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Check if a matching record was found
    if result is None:
        return None, None
    else:
        person, address = result
        return person, address

# Example usage
phone_number = '1234567890'
person, address = connect_number_to_person(phone_number)

if person is None:
    print(f"No information found for phone number: {phone_number}")
else:
    print(f"Phone number: {phone_number}")
    print(f"Person: {person}")
    print(f"Address: {address}")
