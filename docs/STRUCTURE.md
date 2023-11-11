# Ticket Selling Platform Documentation

## Project Structure

This project consists of the following apps:

### Users App: 

Handles user authentication and includes endpoints for user registration, login, and token refresh.

### Stadium App:

Allows the creation of stadiums. Only admins can perform this action, and stadiums can be assigned to matches.

### Match App

Manages the creation of matches and allows admins to assign stadiums to matches.

### Seat App:

Handles the creation of seats, considering stadium capacity, rows, and columns. Only admins can create seats, and they can be assigned to a match.

### Ticketing App:
Manages the buying of tickets. All users can buy tickets.
<br><br><br>
### API Endpoints
<br>

#### Users App

**<span style="color:green;">/api/V1/user/register/:**</span> <span style="color:pink;">User registration.</span>

**<span style="color:green;">/api/V1/user/login/:**</span> <span style="color:pink;">User login.</span>

**<span style="color:green;">/api/V1/user/token/refresh/:**</span> <span style="color:pink;">Token refresh.</span>


#### Stadium App

**<span style="color:green;">/api/V1/stadium/:**</span> <span style="color:pink;">List and create stadiums.</span>

**<span style="color:green;">/api/V1/stadium/<pk>/:**</span> <span style="color:pink;">Retrieve, update, or delete a stadium.</span>

#### Match App

**<span style="color:green;">/api/V1/match/:**</span> <span style="color:pink;">List and create matches.</span>

**<span style="color:green;">/api/V1/match/<pk>/:**</span> <span style="color:pink;">Retrieve, update, or delete a match.</span>

#### Seat App

**<span style="color:green;">/api/V1/seat/:**</span> <span style="color:pink;">List seats.</span>

**<span style="color:green;">/api/V1/seat/<pk>/:**</span> <span style="color:pink;">Retrieve, update, or delete a seat.</span>

#### Ticketing App

**<span style="color:green;">/api/V1/ticketing/buy/:**</span> <span style="color:pink;">Buy new tickets.</span>

#### Admin Panel Routes

**<span style="color:green;">/admin/:**</span> <span style="color:pink;">Django admin panel index.</span>

**<span style="color:green;">/admin/users/user/:**</span> <span style="color:pink;">Manage user information. You must set users to admin with this.</span>

#### Doc Routes

**<span style="color:green;">/docs/:**</span> <span style="color:pink;">Swagger documents.</span>