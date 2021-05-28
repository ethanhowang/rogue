import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler


def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet( # defining the font to use in TCOD
        "dejavu.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler() # used to receive events and process them

    with tcod.context.new_terminal( # clause is responsible for creating aspects of the window pop up
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")
        while True:
                root_console.print(x=player_x, y=player_y, string="@") # telling the command to print "@" on the screen

                context.present(root_console) # for updating the actions it has been told so far

                root_console.clear()  # to prevent trailing after images when moving objects in window

                for event in tcod.event.wait():
                    action = event_handler.dispatch(event) # used to handle keyboard actions and return an action to be processed

                    if action is None:
                        continue

                    if isinstance(action, MovementAction):
                        player_x += action.dx  # for updating the location of the object being moved
                        player_y += action.dy

                    elif isinstance(action, EscapeAction): # when pressing the Esc button, the program exits
                        raise SystemExit()

if __name__ == "__main__":
    main()
