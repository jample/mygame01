# Crossword Game

## How to Play

1. Create a crossword board of a specified size.
2. Add words to the board either horizontally or vertically.
3. Check if the words are valid.
4. Display the game board.

## Game Rules

- Words can be added horizontally or vertically.
- Words cannot overlap unless they share the same letter.
- Words must fit within the boundaries of the board.

## Examples

### Adding Words

```python
crossword = Crossword(5)
crossword.add_word("hello", 0, 0, "horizontal")
crossword.add_word("world", 1, 0, "vertical")
```

### Displaying the Board

```python
crossword.display_board()
```

Output:
```
h e l l o
w
o
r
l
d
```
