import streamlit as st
import random

# Initial settings
GRID_SIZE = 10
WIDTH = 20
HEIGHT = 20
SNAKE_COLOR = 'green'
FOOD_COLOR = 'red'

# Game state
if 'snake' not in st.session_state:
    st.session_state.snake = [(5, 5)]  # Initial snake position
    st.session_state.food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
    st.session_state.direction = "RIGHT"
    st.session_state.game_over = False

# Update the snake position
def move_snake():
    head_x, head_y = st.session_state.snake[0]
    
    if st.session_state.direction == "UP":
        head_y -= 1
    elif st.session_state.direction == "DOWN":
        head_y += 1
    elif st.session_state.direction == "LEFT":
        head_x -= 1
    elif st.session_state.direction == "RIGHT":
        head_x += 1
    
    new_head = (head_x, head_y)
    st.session_state.snake = [new_head] + st.session_state.snake[:-1]

    # Check if snake eats food
    if new_head == st.session_state.food:
        st.session_state.snake.append(st.session_state.snake[-1])  # Grow snake
        st.session_state.food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))

    # Check collision with walls or itself
    if new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in st.session_state.snake[1:]:
        st.session_state.game_over = True

# Display the game grid
def display_game():
    for y in range(HEIGHT):
        row = ""
        for x in range(WIDTH):
            if (x, y) == st.session_state.snake[0]:
                row += "🟩"  # Snake head
            elif (x, y) in st.session_state.snake:
                row += "🟩"  # Snake body
            elif (x, y) == st.session_state.food:
                row += "🟥"  # Food
            else:
                row += "⬛"  # Empty space
        st.write(row)

# Control snake direction using buttons
if not st.session_state.game_over:
    if st.button('Up'):
        if st.session_state.direction != "DOWN":
            st.session_state.direction = "UP"
    if st.button('Down'):
        if st.session_state.direction != "UP":
            st.session_state.direction = "DOWN"
    if st.button('Left'):
        if st.session_state.direction != "RIGHT":
            st.session_state.direction = "LEFT"
    if st.button('Right'):
        if st.session_state.direction != "LEFT":
            st.session_state.direction = "RIGHT"
    
    # Move the snake
    move_snake()
    display_game()
else:
    st.write("Game Over! 🎮")
    if st.button('Restart'):
        # Reset game state
        st.session_state.snake = [(5, 5)]
        st.session_state.food = (random.randint(0, WIDTH-1), random.randint(0, HEIGHT-1))
        st.session_state.direction = "RIGHT"
        st.session_state.game_over = False
        st.session_state.latest_action = 'Game Restarted'

    st.write(st.session_state.latest_action)
