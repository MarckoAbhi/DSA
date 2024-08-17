import chess
import chess.svg

def create_chess(board_size, board_square_size, light_square_color, dark_square_color, piece_color):
    """
    Generate a chessboard SVG image with customizable parameters.

    Parameters:
        - board_size (int): The size of the chessboard (number of squares in each row/column).
        - board_square_size (int): The size of each square on the chessboard.
        - light_square_color (int): Color code for light squares.
        - dark_square_color (int): Color code for dark squares.
        - piece_color (int): Color code for chess pieces.

    Returns:
        str: SVG image as a string.
    """
    # Validate input parameters
    if not all(isinstance(param, int) and param > 0 for param in [board_size, board_square_size]):
        raise ValueError("board_size and board_square_size must be positive integers.")

    board = chess.Board()

    # Convert to CSS colors
    light_square_color = f"#{light_square_color:06x}"
    dark_square_color = f"#{dark_square_color:06x}"
    piece_color = f"#{piece_color:06x}"

    # Generate CSS string
    css = f""".board {{
        width: {board_size}px;
        height: {board_size}px;
        display: grid;
        grid-template-columns: repeat({board_size}, 1fr);
        grid-template-rows: repeat({board_size}, 1fr);
        grid-gap: 0;
    }}
    .square {{
        width: {board_square_size}px;
        height: {board_square_size}px;
        border: none;
    }}
    .light-square {{
        background-color: {light_square_color};
    }}
    .dark-square {{
        background-color: {dark_square_color};
    }}
    .piece {{
        width: {board_square_size}px;
        height: {board_square_size}px;
        display: inline-block;
        vertical-align: top;
        color: {piece_color};
    }}
    """

    # Create SVG image
    svg = chess.svg.board(board=board, size=board_size, style=css)

    return svg

# Test the function
svg = create_chess(800, 100, 0x808080, 0x404040, 0xffffff)
with open("chess.svg", "w") as f:
    f.write(svg)
