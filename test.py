import pygame
import sys


class Game:
    def __init__(self):
        self.player_name = "Player1"
        self.unlocked_class = "Warrior"
        self.save_file_path = "game_save.txt"
        self.font = pygame.font.Font(None, 36)

    def save_game_state(self):
        with open(self.save_file_path, "w") as save_file:
            save_file.write(f"Player: {self.player_name}\n")
            save_file.write(f"Unlocked Class: {self.unlocked_class}\n")

    def load_game_state(self):
        try:
            with open(self.save_file_path, "r") as save_file:
                saved_data = save_file.readlines()
                self.player_name = saved_data[0].split(": ")[1].strip()
                self.unlocked_class = saved_data[1].split(": ")[1].strip()
        except FileNotFoundError:
            print("No saved game state found.")

    def unlock_new_class(self, new_class):
        self.unlocked_class = new_class
        self.save_game_state()


def update_display(screen, game):
    screen.fill((255, 255, 255))

    # Draw unlocked class
    unlocked_text = game.font.render(f"Unlocked Class: {game.unlocked_class}", True, (0, 0, 0))
    screen.blit(unlocked_text, (20, 20))

    # Draw button
    pygame.draw.rect(screen, (0, 255, 0), (150, 100, 100, 50))
    button_text = game.font.render("Unlock", True, (0, 0, 0))
    screen.blit(button_text, (185, 115))


def main():
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    clock = pygame.time.Clock()

    game = Game()
    game.load_game_state()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(150, 100, 100, 50).collidepoint(event.pos):
                    new_class = "Mage"
                    game.unlock_new_class(new_class)
                    print("New class unlocked:", new_class)

        update_display(screen, game)
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()