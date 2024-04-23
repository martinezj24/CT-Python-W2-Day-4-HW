# Task 1: Customer Service Ticket Tracker 

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"},
}

# Function to open a new ticket
def create_ticket(ticket_id, customer, issue):
    if ticket_id not in service_tickets:
        service_tickets[ticket_id] = {'Customer': customer, 'Issue': issue, 'Status': 'open'}
        print(f'Ticket {ticket_id} created')
    else:
        print('Invalid Entry')

# Function to update a ticket status
def update_ticket(ticket_id, new_status):
    if ticket_id in service_tickets:
        service_tickets[ticket_id]['Status'] = new_status
        print(f'Ticket {ticket_id} status updated to {new_status}')
    else:
        print('Invalid Entry')

# Function to display tickets

def display_tickets():
    if service_tickets:
        print(f'All tickets: {service_tickets}')



create_ticket(ticket_id='Ticket003', customer='Joshua', issue= 'Refund Issue')
update_ticket(ticket_id= 'Ticket001', new_status= 'closed')
display_tickets()