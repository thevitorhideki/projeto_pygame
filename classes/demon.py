import pygame

class Demon(pygame.sprite.Sprite):
    """
    A class representing a Demon sprite.
    """

    def __init__(self, speed):
        """
        Construtor da classe Demon.
        """
        super().__init__()
        self.demon_list = [pygame.image.load(f'assets/demon/demon{i}.png').convert_alpha() for i in range(1, 9)]
        # Load the demon images from the 'assets' folder and store them in a list
        # with transparency enabled using convert_alpha()
        self.demon_index = 0
        # Initialize the index of the current demon image
        self.image = self.demon_list[self.demon_index]
        # Set the initial image to the first demon image in the list
        self.rect = self.image.get_rect(bottomleft=(1280 * 3, 620))
        # Create a rect object for the demon image with its initial position
        self.speed = speed

    def animation(self):
        """
        Anima o demônio.
        """
        self.demon_index += 0.1
        # Increment the demon index to animate through the demon images
        self.image = self.demon_list[int(self.demon_index % len(self.demon_list))]
        # Set the current image to the next image in the list, looping back to the beginning if necessary

    def movement(self):
        """
        Move o demônio horizontalmente.
        """
        self.rect.x -= self.speed
        # Move the demon rect horizontally to the left by 4 pixels in each update

    def update(self):
        """
        Atualiza o movimento e a animação do demônio.
        """
        self.movement()
        # Call the movement method to update the demon's position
        self.animation()
        # Call the animation method to update the demon's image

demon = pygame.sprite.GroupSingle()
# Create a sprite group for a single demon object
