# miCRM API

This is the backend API for the proposed miCRM web app. This allows the front end to interface with the database.

### Tables
For now, there are four tables in the database which can be accessed via this API:
1. Users
1. Contacts
1. Meetings
1. FollowUps

For each table, this API will allow items to be created (POST), read (GET), updated (PUT), and deleted (DELETE).

### Implementation Plan:
#### Users
- [x] Define model
- [ ] Create new user
- [ ] Update user
- [ ] Delete user
- [ ] User authentication

#### Contacts
- [x] Define model
- [x] Create new contacts
    - (POST, /contact)
- [x] Delete existing contacts
    - (DELETE, /contact/\<contact_id>)
- [x] Update existing contacts
    - (PUT, /contact/\<contact_id>)
- [x] Read all contacts
    - (GET, /contact)
    - [ ] Add query string capability

#### Meetings
- [ ] Create model
- [ ] CRUD

#### FollowUps
- [ ] Decide if these should just be the same thing and meetings but with a different subtype
